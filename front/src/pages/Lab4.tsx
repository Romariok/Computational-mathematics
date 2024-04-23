import React, { useEffect, useState } from 'react';

import PointTable from '../assets/components/Table';
import Graph from '../assets/components/Graph'
import Box from '@mui/material/Box';

import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Input from '@mui/material/Input';
import Alert from '@mui/material/Alert';
import { Snackbar } from '@mui/material';
import StyleButton from '../assets/components/StyleButton';
import '/src/assets/css/main_page.css'




function Lab4(): JSX.Element {
   const [isOpen, setIsOpen] = useState<boolean>(false);
   const [success, setSuccess] = useState<boolean>(false);
   const [successText, setSuccessText] = useState<string>();
   const [X, setX] = useState<string>("");
   const [Y, setY] = useState<string>("");
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


   const handleSubmitFile = async (e: React.FormEvent<HTMLFormElement>) => {
      playSound();
      console.log("file")
      e.preventDefault();

      setSolution({
         err: "",
         function: "",
         coefficients: [],
         differences: [],
         epsilon_values: [],
         pearson_correlation: 0,
         phi_values: [],
         data_points: [],
         standard_deviation: 0,
         func: "",
      });


      try {
         const response = await fetch(
            "http://127.0.0.1:5000/lab4/file",
            {
               method: "GET"
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
         const x: number[] = data.data_points.map((point: [number, number]) => point[0]);
         const y: number[] = data.data_points.map((point: [number, number]) => point[1]);
         setX(x.join(" "));
         setY(y.join(" "));
         setSolution(data);
         handleOpen();
      } catch (error) {
         console.error(error);
         handleClose();
         setErrorText(`Error while processing: ${error}`);
      }
   };

   const handleSubmitString = async (e: React.FormEvent<HTMLFormElement>) => {
      playSound();
      console.log("string")
      e.preventDefault();

      setSolution({
         err: "",
         function: "",
         coefficients: [],
         differences: [],
         epsilon_values: [],
         pearson_correlation: 0,
         phi_values: [],
         data_points: [],
         standard_deviation: 0,
         func: "",
      });

      const x = X.trim()?.split(" ").map(Number); // Convert string array to number array
      const y = Y.trim()?.split(" ").map(Number); // Convert string array to number array
      console.log(JSON.stringify({ x, y }));

      try {
         const response = await fetch(
            "http://127.0.0.1:5000/lab4/app",
            {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ x, y }),
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
      } catch (error) {
         console.error(error);
         handleClose();
         setErrorText(`Error while processing: ${error}`);
      }
   };

   const handleDownload = async (e: React.FormEvent<HTMLFormElement>) => {
      playSound();
      console.log("download")
      e.preventDefault();


      const x = X.trim()?.split(" ").map(Number); // Convert string array to number array
      const y = Y.trim()?.split(" ").map(Number); // Convert string array to number array

      console.log(JSON.stringify({ x, y, solution }));

      try {
         const response = await fetch(
            "http://127.0.0.1:5000/lab4/download",
            {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ x, y, solution }),
            }
         );

         const data = await response.json();
         console.log(data);

         if (data.error) {
            setErrorText(data.error);
            setError(true);
            return;
         }
         setSuccessText(data.success);
         setSuccess(true);

      } catch (error) {
         console.error(error);
         setError(true);
         setErrorText(`Error while processing: ${error}`);
      }
   };
   return (
      <>
         <Container>
            <header><h1>Lab4 - Approximation</h1></header>
            <Box sx={{
               mt: 1,
               background: 'white', padding: '20px', borderColor: 'white',
               borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
               marginTop: '30px', marginBottom: '30px'
            }}>
               {isOpen && (<Graph fu={solution.function} points={solution.data_points} array={solution.coefficients} />)}
            </Box>

            <Box>
               <Box component="form" noValidate sx={{
                  mt: 1,
                  display: 'flex', flexDirection: 'column', alignItems: 'center',
                  background: 'black', padding: '20px', borderColor: 'white',
                  borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
                  marginTop: '30px', marginBottom: '30px',
               }}>
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="x"
                     name="x"
                     autoComplete="x"
                     autoFocus
                     onChange={(e) => setX(e.target.value)}
                     sx={{ color: 'white', mb: 1 }}
                     placeholder='X'
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="y"
                     name="y"
                     autoComplete="y"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setY(e.target.value)}
                     placeholder='Y'
                  />
                  <Box sx={{ textAlign: 'center' }}>
                     <Grid container sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
                        <Grid item>
                           <StyleButton text={"Submit from File"} type={"button"} onclick={(e) => handleSubmitFile(e as any)} />
                        </Grid>
                        <Grid item>
                           <StyleButton text={"Submit"} type={"button"} onclick={(e) => handleSubmitString(e as any)} />
                        </Grid>
                        {isOpen && (<Grid item>
                           <StyleButton text={"Download"} onclick={(e) => handleDownload(e as any)} type={"button"} />
                        </Grid>)}

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
                     <PointTable array={[solution.coefficients,
                     [solution.func], [solution.standard_deviation],
                     [solution.pearson_correlation], solution.differences,
                     solution.phi_values, solution.epsilon_values]} />
                  </Box>
               )}
            </Box>
         </Container>
      </>
   )
}

export default Lab4;
