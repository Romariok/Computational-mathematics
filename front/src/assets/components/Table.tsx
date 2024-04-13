import React, { useEffect } from 'react';
import { TableBody, TableCell, TableContainer, TableHead, TableRow, Table } from '@mui/material';
import { useSelector } from 'react-redux';
// import { appSelector } from '../../storage/slices/AppSlice';

interface Row {
    x: number;
    y: number;
    r: number;
    result: boolean;
}

const PointTable: React.FC = () => {
   //  const { array } = useSelector(appSelector);
    const token = localStorage.getItem("token");

    useEffect(() => {
        console.log(array);
    }, [array]);

    if (!!token && array.length !== 0) {
        return (
            <TableContainer className='main__table-container'>
                <Table className="main__table" aria-label="data table">
                    <TableHead>
                        <TableRow>
                            <TableCell>X</TableCell>
                            <TableCell>Y</TableCell>
                            <TableCell>R</TableCell>
                            <TableCell>STATUS</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {array.map((row: Row, i: number) => (
                            <TableRow key={i}>
                                <TableCell>{row.x}</TableCell>
                                <TableCell>{row.y}</TableCell>
                                <TableCell>{row.r}</TableCell>
                                <TableCell>{row.result ? "Yes" : "No"}</TableCell>
                            </TableRow>
                        )).reverse()}
                    </TableBody>
                </Table>
            </TableContainer>
        );
    } else {
        return (
            <TableContainer className='main__table-container'>
                <Table className="main__table" aria-label="data table">
                    <TableHead>
                        <TableRow>
                            <TableCell>X</TableCell>
                            <TableCell>Y</TableCell>
                            <TableCell>R</TableCell>
                            <TableCell>STATUS</TableCell>
                        </TableRow>
                    </TableHead>
                </Table>
            </TableContainer>
        );
    }
}

export default PointTable;
