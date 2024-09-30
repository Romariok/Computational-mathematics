import { useState, useRef, useEffect } from 'react';




export default function Graph({ fu, euler, ext_euler, milne, direct}: { fu: number; euler: number[][]; ext_euler:number[][];milne: number[][]; direct:number[][]}) {
    const width = 600, height = 600

    const canvasRef = useRef<HTMLCanvasElement | null>(null);

    function calculateInitialBounds(points: number[][]) {
        if (points && points.length > 0) {
            const xValues = points.map(point => point[0]);
            const yValues = points.map(point => point[1]);

            return {
                xmin: -(Math.max(Math.abs(Math.min(...xValues)), Math.max(...xValues)) + 0.3),
                xmax: (Math.max(Math.abs(Math.min(...xValues)), Math.max(...xValues)) + 0.3),
                ymin: -(Math.max(Math.abs(Math.min(...yValues)), Math.max(...yValues)) + 0.3),
                ymax: (Math.max(Math.abs(Math.min(...yValues)), Math.max(...yValues)) + 0.3),
            };
        }
        // Возвращаем значения по умолчанию, если нет точек
        return { xmin: -100, xmax: 100, ymin: -100, ymax: 100 };
    }

    // Используем функцию для инициализации состояния bounds
    const [bounds, setBounds] = useState(() => calculateInitialBounds(milne));
    const f = (point:number[]) => {
        switch (fu) {
            case 1:
                return -2*point[1] + point[0] * point[0];
            case 2:
                return (2*point[0] + 4 * point[1] - 3)/(point[0] + 2*point[1] + 1);
            case 3:
                return point[1] * Math.cos(point[0]);
            default:
                return Math.random() * 100;
        }
    };

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
        setBounds(calculateInitialBounds(milne));
        const canvas = canvasRef.current;
        if (!canvas) return;
        const context = canvas.getContext('2d');
        drawGraph(context, bounds);
    }, [milne]);

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

        if (direct && direct.length){
            ctx.beginPath();
            ctx.strokeStyle = 'red';
            for (let i = 0; i<direct.length; i+=1){
                const x = offsetX + (direct[i][0] * scaleX);
                const y = offsetY - (direct[i][1] * scaleY);
                if (i === 0){
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
                
            }
            ctx.stroke();
        }


        if (euler && euler.length) {
            ctx.fillStyle = 'blue'; 
            euler.forEach(point => {
                const x = offsetX + (point[0] * scaleX);
                const y = offsetY - (point[1] * scaleY);
                ctx.beginPath(); 
                ctx.arc(x, y, 2, 0, 2 * Math.PI); 
                ctx.fill();
            });
        }
        if (ext_euler && ext_euler.length) {
            ctx.fillStyle = 'green'; 
            ext_euler.forEach(point => {
                const x = offsetX + (point[0] * scaleX);
                const y = offsetY - (point[1] * scaleY);
                ctx.beginPath(); 
                ctx.arc(x, y, 2, 0, 2 * Math.PI); 
                ctx.fill();
            });
        }
        if (milne && milne.length) {
            ctx.fillStyle = 'cyan'; 
            milne.forEach(point => {
                const x = offsetX + (point[0] * scaleX);
                const y = offsetY - (point[1] * scaleY);
                ctx.beginPath(); 
                ctx.arc(x, y, 2, 0, 2 * Math.PI); 
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
