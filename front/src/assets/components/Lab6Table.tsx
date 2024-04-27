import { TableBody, TableCell, TableContainer, TableHead, TableRow, TableBodyClasses, Table, Typography} from '@mui/material';
import 'katex/dist/katex.min.css';
import { InlineMath } from 'react-katex';


export default function PointTable({ array0, array1, array2 }: { array0: any[][] | undefined, array1: any[][] | undefined, array2: any[][] | undefined}) {
    if (array0 !== undefined && array1 !== undefined && array2 !== undefined) {
        return (
            <TableContainer className='main__table-container' >
               <Typography variant="body1" sx={{ color: 'white', fontFamily: "Undertale" }}>Метод Эйлера</Typography>
                <Table className="main__table" aria-label="data table" sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                <TableHead>
                  <TableRow>
                     <TableCell>X</TableCell>
                     <TableCell>Y</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
               {array0.map((row, index) => (
                  <TableRow key={index}>
                  <TableCell>{row[0]}</TableCell>
                  <TableCell>{row[1]}</TableCell>
                  </TableRow>
               ))}
               </TableBody>
               </Table>
               <Typography variant="body1" sx={{ color: 'white', fontFamily: "Undertale" }}>Усовершенствованный метод Эйлера</Typography>
                <Table className="main__table" aria-label="data table" sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                <TableHead>
                  <TableRow>
                     <TableCell>X</TableCell>
                     <TableCell>Y</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
               {array1.map((row, index) => (
                  <TableRow key={index}>
                  <TableCell>{row[0]}</TableCell>
                  <TableCell>{row[1]}</TableCell>
                  </TableRow>
               ))}
               </TableBody>
               </Table>
               <Typography variant="body1" sx={{ color: 'white', fontFamily: "Undertale" }}>Метод Милна</Typography>
                <Table className="main__table" aria-label="data table" sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                <TableHead>
                  <TableRow>
                     <TableCell>X</TableCell>
                     <TableCell>Y</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
               {array1.map((row, index) => (
                  <TableRow key={index}>
                  <TableCell>{row[0]}</TableCell>
                  <TableCell>{row[1]}</TableCell>
                  </TableRow>
               ))}
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


