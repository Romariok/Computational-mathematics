import { useState, useRef, useEffect } from 'react';




export default function Graph({points}: {points: number[][]}) {
    const width = 600, height = 600

    const canvasRef = useRef<HTMLCanvasElement | null>(null);

    function calculateInitialBounds(points: number[][]) {
        if (points && points.length > 0) {
            const xValues = points.map(point => point[0]);
            const yValues = points.map(point => point[1]);

            return {
                xmin: -(Math.max(Math.abs(Math.min(...xValues)), Math.max(...xValues)) + 6),
                xmax: (Math.max(Math.abs(Math.min(...xValues)), Math.max(...xValues)) + 6),
                ymin: -(Math.max(Math.abs(Math.min(...yValues)), Math.max(...yValues)) + 6),
                ymax: (Math.max(Math.abs(Math.min(...yValues)), Math.max(...yValues)) + 6),
            };
        }
        // Возвращаем значения по умолчанию, если нет точек
        return { xmin: -100, xmax: 100, ymin: -100, ymax: 100 };
    }

    // Используем функцию для инициализации состояния bounds
    const [bounds, setBounds] = useState(() => calculateInitialBounds(points));

    function diff(k: number, i: number, x: number[], y: number[]): number {
      const n = x.length;
      if (k === 0) {
        return y[i];
      } else if (i + k >= n) {
        throw new Error("Index out of bounds");
      } else {
        return (diff(k - 1, i + 1, x, y) - diff(k - 1, i, x, y)) / (x[i + k] - x[i]);
      }
    }
    
    function newton(v: number): number {
      if (!points || !points[0]){
         return Math.random() * 100;
      }
      
      let x = points.map(point => point[0]);
      let y = points.map(point => point[1]);
      const n = x.length;
      let sum = y[0];
      for (let i = 1; i < n; i++) {
        let product = 1.0;
        for (let j = 0; j < i; j++) {
          product *= v - x[j];
        }
        sum += diff(i, 0, x, y) * product;
      }
      return sum;
    }

    function factorial(n: number): number {
      if (n === 0 || n === 1) {
        return 1;
      }
      return n * factorial(n - 1);
    }

    function differenceTable(): number[][] {
      if (!points){
         return [[]];
      }
      let y = points.map(point => point[1]);
      const n = y.length;
      const defy: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    
      for (let i = 0; i < n; i++) {
        defy[i][0] = y[i];
      }
    
      for (let i = 1; i < n; i++) {
        for (let j = 0; j < n - i; j++) {
          defy[j][i] = defy[j + 1][i - 1] - defy[j][i - 1];
        }
      }
    
      return defy
    }

    function gauss(v: number, h: number, defy: number[][]): number {
      if (!points){
        return Math.random() * 100;
      }
      let x = points.map(point => point[0]);
      let y = points.map(point => point[1]);
      const a = Math.floor(y.length / 2);
      let t = 0.0;
      let tn = 0.0;
      let pn = 0.0;
      let fact = 0.0; 
      let n = 0.0;
      if (v > x[a]) {
        t = (v - x[a]) / h;
        n = defy.length;
        pn = defy[a][0] + t * defy[a][1] + ((t * (t - 1)) / 2) * defy[a - 1][2];
        let tn = t * (t - 1);
        for (let i = 3; i < n; i++) {
          if (i % 2 === 1) {
            n = Math.floor((i + 1) / 2);
            tn *= (t + n - 1);
            pn += ((tn / factorial(i)) * defy[a - n + 1][i]);
          } else {
            n = i / 2;
            tn *= (t - n);
            pn += ((tn / factorial(i)) * defy[a - n][i]);
          }
        }
      } else if (v < x[a]) {
        t = (v - x[a]) / h;
        n = defy.length;
        pn = defy[a][0] + t * defy[a - 1][1] + ((t * (t + 1)) / 2) * defy[a - 1][2];
        tn = t * (t + 1);
        for (let i = 3; i < n; i++) {
          if (i % 2 === 1) {
            n = Math.floor((i + 1) / 2);
            tn *= (t + n - 1);
          } else {
            n = i / 2;
            tn *= (t - n);
          }
          fact = factorial(i);
          pn += (tn / fact) * defy[a - n][i];
        }
      } else {
        throw  Error("Error in Gauss");
      }
      return pn;
    }

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const handleMouseMove = (event: { clientX: number; clientY: number; }) => {
            const rect = canvas.getBoundingClientRect();
            const scaleX = width / (bounds.xmax - bounds.xmin);
            const scaleY = height / (bounds.ymax - bounds.ymin);
            const canvasX = event.clientX - rect.left;
            const canvasY = event.clientY - rect.top;
            const graphX = (canvasX / scaleX) + bounds.xmin;
            const graphY = bounds.ymax - (canvasY / scaleY);
            setCursorPosition({ x: graphX, y: graphY });
        };

        const boundsAreValid = Math.abs(bounds.xmin) === Math.abs(bounds.xmax) && Math.abs(bounds.ymin) === Math.abs(bounds.ymax);

        if (boundsAreValid) {
            canvas.addEventListener('mousemove', handleMouseMove);
        } else {
            setCursorPosition({ x: 0, y: 0 });
        }

        return () => {
            if (boundsAreValid) {
                canvas.removeEventListener('mousemove', handleMouseMove);
            }
        };
    }, [bounds]);

    useEffect(() => {
        setBounds(calculateInitialBounds(points));
        const canvas = canvasRef.current;
        if (!canvas) return;
        const context = canvas.getContext('2d');
        drawGraph(context, bounds);
    }, [points]);

    const drawGraph = (ctx: CanvasRenderingContext2D | null, bounds: { xmin: any; xmax: any; ymin: any; ymax: any; }) => {
        if (!ctx) return;
        const scaleX = width / (bounds.xmax - bounds.xmin);
        const scaleY = height / (bounds.ymax - bounds.ymin);

        const offsetX = width / 2;
        const offsetY = height / 2;
        ctx.clearRect(0, 0, width, height); // Очищаем canvas

        // Рисуем оси
        ctx.beginPath();
        ctx.moveTo(0, offsetY);
        ctx.lineTo(width, offsetY);
        ctx.moveTo(offsetX, 0);
        ctx.lineTo(offsetX, height);
        ctx.strokeStyle = 'black';
        ctx.stroke();

        // Функция для добавления делений и значений на оси
        const drawAxisLabels = () => {
            const tickSize = 5;
            let stepX, stepY;

            // Определяем шаг на основе диапазона значений
            if (bounds.xmin > -6 && bounds.xmax < 6) {
                stepX = 0.2;
                stepY = 0.2; // Пример, можно настроить отдельно для оси Y
            } else {
                stepX = (bounds.xmax - bounds.xmin) / 20; // Более крупный шаг для больших диапазонов
                stepY = (bounds.ymax - bounds.ymin) / 20; // Аналогично для оси Y
            }

            ctx.font = '10px Arial';
            ctx.fillStyle = 'black';
            ctx.textAlign = 'center';

            // Деления и значения по оси X
            for (let xValue = -1000; xValue <= 1000; xValue += stepX) {
                const x = offsetX + (xValue * scaleX);
                ctx.moveTo(x, offsetY - tickSize);
                ctx.lineTo(x, offsetY + tickSize);
                ctx.fillText(xValue.toFixed(1), x, offsetY + tickSize + 10);
            }

            // Деления и значения по оси Y
            for (let yValue = -1000; yValue <= 1000; yValue += stepY) {
                if (Math.abs(yValue) >= 0.1) { // Подписываем только целые числа
                    const y = offsetY - (yValue * scaleY);
                    ctx.moveTo(offsetX - tickSize, y);
                    ctx.lineTo(offsetX + tickSize, y);
                    ctx.fillText(yValue.toFixed(1), offsetX - tickSize - 10, y + 3);
                }
            }

            ctx.stroke();
        };

        drawAxisLabels();

        // Рисуем график
        ctx.beginPath();
        ctx.strokeStyle = 'green';
        for (let i = bounds.xmin; i <= bounds.xmax; i += (bounds.xmax - bounds.xmin) / width) {
            const x = offsetX + (i * scaleX);
            const y = offsetY - (newton(i) * scaleY);
            if (i === bounds.xmin) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        let h = 0.0
        ctx.stroke();
        if (points && points[0]){
         h = points[1][0] - points[0][0];
        }

        ctx.beginPath();
        ctx.strokeStyle = 'red';
        for (let i = bounds.xmin; i <= bounds.xmax; i += (bounds.xmax - bounds.xmin) / width) {
            const x = offsetX + (i * scaleX);
            const y = offsetY - (gauss(i, h, differenceTable()) * scaleY);
            if (i === bounds.xmin) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();

        if (points && points.length) {
            ctx.fillStyle = 'blue'; // Цвет для точек
            points.forEach(point => {
                const x = offsetX + (point[0] * scaleX);
                const y = offsetY - (point[1] * scaleY);
                ctx.beginPath(); // Начинаем новый путь для каждой точки
                ctx.arc(x, y, 2, 0, 2 * Math.PI); // Рисуем круг радиусом 5
                ctx.fill();
            });
        }
    };


    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const context = canvas.getContext('2d');
        drawGraph(context, bounds);
    }, [bounds]);

    const [cursorPosition, setCursorPosition] = useState({ x: 0, y: 0 });

    return (
        <div className="graph" >
            <div className="center-container">
                <canvas ref={canvasRef} width={width} height={height} />
            </div>
            <p>X: {cursorPosition.x.toFixed(2)}, Y: {cursorPosition.y.toFixed(2)}</p>
        </div>
    );
};
