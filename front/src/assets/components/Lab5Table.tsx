import { TableBody, TableCell, TableContainer, TableHead, TableRow, TableBodyClasses, Table} from '@mui/material';
import 'katex/dist/katex.min.css';
import { InlineMath } from 'react-katex';


export default function PointTable({ array, values }: { array: any[][] | undefined, values: any[] | undefined }) {
    if (array !== undefined) {
        return (
            <TableContainer className='main__table-container' >
                <Table className="main__table" aria-label="data table" sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                    <TableHead>
                    
                        <TableRow>
                            {array[0].map((_, index) => (
                            <TableCell key={index}><InlineMath math={index ? `\\Delta^${index}y_i` : `y_i`}/></TableCell>
                            ))}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                    {array.map((row, rowIndex) => (
                        <TableRow key={rowIndex}>
                        {row.map((cell, cellIndex) => (
                            <TableCell key={`${rowIndex}-${cellIndex}`}>{cell}</TableCell>
                        ))}
                        </TableRow>
                    ))}
                    </TableBody>
                </Table>

                <Table className="main__table" aria-label="data table" sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                    <TableHead>
                        <TableRow>
                            <TableCell>Lagrange</TableCell>
                            <TableCell>Newton 🟢</TableCell>
                            <TableCell>Gauss 🔴</TableCell>
                            <TableCell>Sterling</TableCell>
                            <TableCell>Bessel</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>

                        <TableRow key={0}>
                        {values.map((cell, cellIndex) => (
                            <TableCell key={`${cellIndex}`}>{cell}</TableCell>
                        ))}
                        </TableRow>
                    </TableBody>
                </Table>
            </TableContainer>



        );
    } else {
        return(
            {

            }
        );
    }
}


