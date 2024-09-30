import React, {useState } from 'react';

import PointTable from '../assets/components/Lab5Table';
import Graph from '../assets/components/Graph5'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import 'katex/dist/katex.min.css';
import { InlineMath } from 'react-katex';

import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Input from '@mui/material/Input';
import Alert from '@mui/material/Alert';
import { Snackbar } from '@mui/material';
import StyleButton from '../assets/components/StyleButton';
import '/src/assets/css/main_page.css'




function Lab5(): JSX.Element {
   const [isOpen, setIsOpen] = useState<boolean>(false);
   const [success, setSuccess] = useState<boolean>(false);
   const [successText, setSuccessText] = useState<number>();
   const [X, setX] = useState<string>("");
   const [Y, setY] = useState<string>("");
   const [N, setN] = useState<number>(0);
   const [A, setA] = useState<number>(0);
   const [B, setB] = useState<number>(0);
   const [VALUE, setValue] = useState<number>(0);
   const [numFile, setNumFile] = useState<number>(0);
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


   const handleSubmitFunc = async (e: React.FormEvent<HTMLFormElement>) => {
      playSound();
      console.log("func")
      e.preventDefault();
      setSolution({
         err: "",
         data_points: [],
         values: [],
         defy: [[]]
      });

      const n = N
      const a = A
      const b = B
      const num = numFunc
      const value = VALUE
      console.log(num, value)
      try {
         const response = await fetch(
            "http://127.0.0.1:5000/lab5/function",
            {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ num, value, n, a, b }),
            }
         );

         const data = await response.json();
         

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
         console.log(data);
         setSolution(data);
         console.log(solution);
         handleOpen();
      } catch (error) {
         console.error(error);
         handleClose();
         setErrorText(`Error while processing: ${error}`);
      }
   };

   const handleSubmitFile = async (e: React.FormEvent<HTMLFormElement>) => {
      playSound();
      console.log("file")
      e.preventDefault();

      setSolution({
         err: "",
         data_points: [],
         values: [],
         defy: [[]]
      });

      const num = numFile
      const value = VALUE
      console.log(num, value)
      try {
         const response = await fetch(
            "http://127.0.0.1:5000/lab5/file",
            {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ num, value }),
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
         data_points: [],
         values: [],
         defy: [[]]
      });

      const x = X.trim()?.split(" ").map(Number); // Convert string array to number array
      const y = Y.trim()?.split(" ").map(Number); // Convert string array to number array
      const value = Number(VALUE)
      console.log(JSON.stringify({ x, y, value }));

      try {
         const response = await fetch(
            "http://127.0.0.1:5000/lab5/app",
            {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ x, y, value }),
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

   return (
      <>
         <Container>
            <header><h1>Lab5 - Interpolation</h1></header>
            <Box sx={{
               mt: 1,
               background: 'white', padding: '20px', borderColor: 'white',
               borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
               marginTop: '30px', marginBottom: '30px'
            }}>
               {isOpen && (<Graph points={solution.data_points}/>)}
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
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="value"
                     name="value"
                     autoComplete="value"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setValue(Number(e.target.value))}
                     placeholder='VALUE'
                     inputProps={{ min: -100000, max: 100000 }}
                     type='number'
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
                     id="numFile"
                     name="numFile"
                     autoComplete="numFile"
                     autoFocus
                     onChange={(e) => setNumFile(Number(e.target.value))}
                     sx={{ color: 'white', mb: 1 }}
                     placeholder='Number of File'
                     inputProps={{ min: 1, max: 3 }}
                     type='number'
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="value"
                     name="value"
                     autoComplete="value"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setValue(Number(e.target.value))}
                     placeholder='VALUE'
                     inputProps={{ min: -100000, max: 100000 }}
                     type='number'
                  />
                  <Box sx={{ textAlign: 'center' }}>
                     <Grid container sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
                        <Grid item>
                           <StyleButton text={"Submit from File"} type={"button"} onclick={(e) => handleSubmitFile(e as any)} />
                        </Grid>
                     </Grid>
                  </Box>
               </Box>



               <Box component="form" noValidate sx={{
                  mt: 1,
                  display: 'flex', flexDirection: 'column', alignItems: 'center',
                  background: 'black', padding: '20px', borderColor: 'white',
                  borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
                  marginTop: '30px', marginBottom: '30px',
               }}>
                  <Typography variant="body1" sx={{ color: 'white', fontFamily: "Undertale" }}><InlineMath math={`1) 2\\cdot\\sin{x} - 4 \\quad \\quad 2) 13 - 5\\cdot\\cos{x}`}/></Typography>
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="n"
                     name="n"
                     autoComplete="n"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setN(Number(e.target.value))}
                     placeholder='N'
                     inputProps={{ min: -100000, max: 100000 }}
                     type='number'
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="a"
                     name="a"
                     autoComplete="a"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setA(Number(e.target.value))}
                     placeholder='A'
                     inputProps={{ min: -100000, max: 100000 }}
                     type='number'
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="b"
                     name="b"
                     autoComplete="b"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setB(Number(e.target.value))}
                     placeholder='B'
                     inputProps={{ min: -100000, max: 100000 }}
                     type='number'
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="value"
                     name="value"
                     autoComplete="value"
                     autoFocus
                     sx={{ color: 'white' }}
                     onChange={(e) => setValue(Number(e.target.value))}
                     placeholder='VALUE'
                     inputProps={{ min: -100000, max: 100000 }}
                     type='number'
                  />
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="numFile"
                     name="numFile"
                     autoComplete="numFile"
                     autoFocus
                     onChange={(e) => setNumFunc(Number(e.target.value))}
                     sx={{ color: 'white', mb: 1 }}
                     placeholder='Number of Function'
                     inputProps={{ min: 1, max: 2 }}
                     type='number'
                  />
                  <Box sx={{ textAlign: 'center' }}>
                     <Grid container sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
                        <Grid item>
                           <StyleButton text={"Submit Function"} type={"button"} onclick={(e) => handleSubmitFunc(e as any)} />
                        </Grid>
                     </Grid>
                  </Box>
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
                     {isOpen && (<PointTable array={solution.defy} values ={solution.values} />)}
                  </Box>
               )}
            </Box>
         </Container>
      </>
   )
}

export default Lab5;
