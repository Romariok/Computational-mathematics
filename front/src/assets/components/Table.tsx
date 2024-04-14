import { TableBody, TableCell, TableContainer, TableHead, TableRow, Table, Stack } from '@mui/material';



export default function PointTable({ array }: { array: any[][] }) {


    if (array.length !== 0) {
        return (
            <TableContainer className='main__table-container' >
                <Table className="main__table" aria-label="data table" sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                    <TableHead>
                        <TableRow>
                            <TableCell>Coefficients</TableCell>
                            <TableCell>{array[0]}</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        <TableRow>
                            <TableCell>Function</TableCell>
                            <TableCell>{array[1]}</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>Standart Deviation</TableCell>
                            <TableCell>{array[2]}</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>Pearson correlation</TableCell>
                            <TableCell>{array[3]}</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>Differences</TableCell>
                            <TableCell>{array[4]}</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>Phi values</TableCell>
                            <TableCell>{array[5]}</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>Epsilon values</TableCell>
                            <TableCell>{array[6]}</TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </TableContainer>


        );
    } else {
        return (
            <TableContainer className='main__table-container' sx={{ maxWidth: '100%', overflowX: 'auto' }}>
                <Table className="main__table" aria-label="data table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Coefficients</TableCell>
                            <TableCell>Function</TableCell>
                            <TableCell>Standart Deviation</TableCell>
                            <TableCell>Pearson correlation</TableCell>
                            <TableCell>Differences</TableCell>
                            <TableCell>Phi Values</TableCell>
                            <TableCell>Epsilon Values</TableCell>
                        </TableRow>
                    </TableHead>
                </Table>
            </TableContainer>
        );
    }
}


