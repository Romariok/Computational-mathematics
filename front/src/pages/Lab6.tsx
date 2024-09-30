import React, {useState } from 'react';

import PointTable from '../assets/components/Lab6Table';
import Graph from '../assets/components/Graph6'
import Box from '@mui/material/Box';

import 'katex/dist/katex.min.css';
import { InlineMath } from 'react-katex';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Input from '@mui/material/Input';
import Alert from '@mui/material/Alert';
import { Snackbar } from '@mui/material';
import StyleButton from '../assets/components/StyleButton';
import '/src/assets/css/main_page.css'




function Lab5(): JSX.Element {
   const [isOpen, setIsOpen] = useState<boolean>(false);
   const [success, setSuccess] = useState<boolean>(false);
   const [successText, setSuccessText] = useState<number>();
   const [X0, setX0] = useState<number>(0);
   const [Y0, setY0] = useState<number>(0);
   const [XN, setXN] = useState<number>(0);
   const [E, setE] = useState<number>(0);
   const [H, setH] = useState<number>(0);
   const [numFunc, setNumFunc] = useState<number>(0);
   const [solution, setSolution] = useState<any>("");
   const [error, setError] = useState<boolean>(false);
   const [errorText, setErrorText] = useState<string>();

   const handleOpen = () => {
      setIsOpen(true);
   };

   const handleClose = () => {
      setIsOpen(false);
   };
   const ring = new Audio('src/assets/sounds/ring.mp3');

   const playSound = () => {
      ring.play();
   };


   const handleSubmitString = async (e: React.FormEvent<HTMLFormElement>) => {
      playSound();
      console.log("string")
      e.preventDefault();
      setSolution({
         "euler": [],
         "ext_euler": [],
         "milne": [],
         "direct": []
      });

      const eq_num = numFunc; 
      const x0 = X0; 
      const xn = XN; 
      const y0 = Y0;
      const eps = E;
      const h = H;




      console.log(JSON.stringify({ eq_num, x0, xn, y0, eps, h }));


         const response = await fetch(
            "http://127.0.0.1:5000/lab6/app",
            {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ eq_num, x0, xn, y0, eps, h  }),
            }
         );

         const data = await response.json();
         console.log(data);

         if (data.error) {
            handleClose();
            setErrorText(data.error);
            setError(true);
            return;
         }
         setSolution(data);
         handleOpen();

   };

   return (
      <>
         <Container>
            <header><h1>Lab6 - NUMERICAL SOLUTION OF ORDINARY
DIFFERENTIAL EQUATIONS</h1></header>
            <Box sx={{
               mt: 1,
               background: 'white', padding: '20px', borderColor: 'white',
               borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
               marginTop: '30px', marginBottom: '30px'
            }}>
               {isOpen && (<Graph fu={numFunc} euler={solution.euler} ext_euler={solution.ext_euler} milne={solution.milne} direct={solution.direct}/>)}
            </Box>

            <Box>
               <Box component="form" noValidate sx={{
                  mt: 1,
                  display: 'flex', flexDirection: 'column', alignItems: 'center',
                  background: 'black', padding: '20px', borderColor: 'white',
                  borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
                  marginTop: '30px', marginBottom: '30px',
               }}>
                  <Typography variant="body1" sx={{ color: 'white', fontFamily: "Undertale" }}><InlineMath math={`1) 4\\cdot x + \\cfrac{y}{3} \\quad \\quad 2) x^2 + y \\quad \\quad 3) y \\cdot \\cos{x}`}/></Typography>
                   <Input
                     margin="dense"
                     required
                     fullWidth
                     id="funcNum"
                     name="funcNum"
                     autoComplete="funcNum"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setNumFunc(Number(e.target.value))}
                     placeholder='Function number'
                     type='number'
                     inputProps={{ min: 1, max: 3 }}
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="x0"
                     name="x0"
                     autoComplete="x0"
                     autoFocus
                     onChange={(e) => setX0(Number(e.target.value))}
                     sx={{ color: 'white', mb: 1 }}
                     placeholder='X0'
                     type='number'
                     inputProps={{ min: -100, max: 100 }}
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="xn"
                     name="xn"
                     autoComplete="xn"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setXN(Number(e.target.value))}
                     placeholder='XN'
                     type='number'
                     inputProps={{ min: -100, max: 100 }}
                  />
                   <Input
                     margin="dense"
                     required
                     fullWidth
                     id="y0"
                     name="y0"
                     autoComplete="y0"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setY0(Number(e.target.value))}
                     placeholder='Y0'
                     type='number'
                     inputProps={{ min: -100, max:100 }}
                  />
                   <Input
                     margin="dense"
                     required
                     fullWidth
                     id="e"
                     name="e"
                     autoComplete="e"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setE(Number(e.target.value))}
                     placeholder='E'
                     type='number'
                     inputProps={{ min: 0.0000001, max: 100 }}
                  />
                   <Input
                     margin="dense"
                     required
                     fullWidth
                     id="h"
                     name="h"
                     autoComplete="h"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setH(Number(e.target.value))}
                     placeholder='H'
                     type='number'
                     inputProps={{ min: 0.0000000001, max: 100 }}
                  />

                  <Box sx={{ textAlign: 'center' }}>
                     <Grid container sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
                        <Grid item>
                           <StyleButton text={"Submit"} type={"button"} onclick={(e) => handleSubmitString(e as any)} />
                        </Grid>
                     </Grid>
                  </Box>
                  <Snackbar open={error} autoHideDuration={3000} onClose={() => setError(false)}>
                     <Alert severity="error" sx={{ fontFamily: "Undertale" }}>
                        {errorText}
                     </Alert>
                  </Snackbar>
                  <Snackbar open={success} autoHideDuration={3000} onClose={() => setSuccess(false)}>
                     <Alert severity="success" sx={{ fontFamily: "Undertale" }}>
                        {successText}
                     </Alert>
                  </Snackbar>
               </Box>
            </Box>
            <Box sx={{
               mt: 1,
               background: 'black', padding: '20px', borderColor: 'white',
               borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
               marginTop: '30px', marginBottom: '30px'
            }}>
               {(

                  <Box sx={{ display: 'flex', alignItems: 'center', overflowX: 'hidden' }}>
                     {isOpen && (<PointTable array0={solution.euler} array1={solution.ext_euler} array2={solution.milne} />)}
                  </Box>
               )}
            </Box>
         </Container>
      </>
   )
}

export default Lab5;
