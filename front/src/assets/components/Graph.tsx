import { useState, useRef, useEffect } from 'react';




export default function Graph({ fu, points, array }: { fu: string; points: number[][]; array: number[] }) {
    // const width = 900, height =900
    const width = 600, height = 600

    const canvasRef = useRef<HTMLCanvasElement | null>(null);

    function calculateInitialBounds(points: number[][]) {
        if (points && points.length > 0) {
            const xValues = points.map(point => point[0]);
            const yValues = points.map(point => point[1]);

            return {
                xmin: -(Math.max(Math.abs(Math.min(...xValues)), Math.max(...xValues)) + 10),
                xmax: (Math.max(Math.abs(Math.min(...xValues)), Math.max(...xValues)) + 10),
                ymin: -(Math.max(Math.abs(Math.min(...yValues)), Math.max(...yValues)) + 10),
                ymax: (Math.max(Math.abs(Math.min(...yValues)), Math.max(...yValues)) + 10),
            };
        }
        // Возвращаем значения по умолчанию, если нет точек
        return { xmin: -100, xmax: 100, ymin: -100, ymax: 100 };
    }

    // Используем функцию для инициализации состояния bounds
    const [bounds, setBounds] = useState(() => calculateInitialBounds(points));
    const f = (x: number) => {
        switch (fu) {
            case "0":
                return array[1] * x + array[0];
            case "1":
                return array[2] * x * x + array[1] * x + array[0];
            case "2":
                return array[3] * x * x * x + array[2] * x * x + array[1] * x + array[0];
            case "3":
                return array[0] * Math.exp(array[1] * x);
            case "4":
                return array[1] * Math.log(x) + array[0];
            case "5":
                return array[0] * Math.pow(x, array[1]);
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
        setBounds(calculateInitialBounds(points));
        const canvas = canvasRef.current;
        if (!canvas) return;
        const context = canvas.getContext('2d');
        drawGraph(context, bounds);
    }, [array]);

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
        ctx.strokeStyle = 'red';
        for (let i = bounds.xmin; i <= bounds.xmax; i += (bounds.xmax - bounds.xmin) / width) {
            const x = offsetX + (i * scaleX);
            const y = offsetY - (f(i) * scaleY);
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
