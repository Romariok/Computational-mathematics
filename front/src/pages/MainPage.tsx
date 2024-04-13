import React, { useEffect, useState } from 'react';


import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Input from '@mui/material/Input';
import Alert from '@mui/material/Alert';
import { Snackbar } from '@mui/material';
import { useMediaQuery } from '@mui/material';
import StyleButton from '../assets/components/StyleButton';
import '/src/assets/css/main_page.css'




function MainPage(): JSX.Element {
   const [X, setX] = useState<string>("");
   const [Y, setY] = useState<string>("");
   const [solution, setSolution] = useState<any>("");
   const [error, setError] = useState<boolean>(false);
   const [errorText, setErrorText] = useState<string>();
   var elt = document.getElementById('calculator')!;
   var calculator = Desmos.GraphingCalculator(elt)

   const ring = new Audio('src/assets/sounds/ring.mp3');

   const playSound = () => {
      ring.play();
   };

   const handleSubmitString = async (e: React.FormEvent<HTMLFormElement>) => {
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
            //  handleOpen();
            setErrorText(data.error);
            setError(true);
            return;
         }

         setSolution(data.result);
         //   setSolutionFile(data);
      } catch (error) {
         console.error(error);
         //   handleOpen();
         setErrorText(`Error while processing: ${error}`);
      }
   };
   const isDesktop = useMediaQuery('(min-width: 1260px)');
   const isTablet = useMediaQuery('(min-width: 781px) and (max-width: 1259px)');
   const isMobile = useMediaQuery('(max-width: 780px)');
   return (
      <>
         <Container
            maxWidth={'xs'}
            sx={{
               height: isDesktop ? '100vh' : isTablet ? '50vh' : isMobile ? '100vh' : '100vh',
               width: isDesktop ? '100vw' : isTablet ? '100vw' : isMobile ? '100vw' : '100vw'
            }}
         >
            <header><h1>Lab4 - Approximation</h1></header>
            <Box sx={{
               mt: 1,

               background: 'black', padding: '20px', borderColor: 'white',
               borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
               marginTop: '30px', marginBottom: '30px',
            }}>
               <div id="calculator" style={{ width: "300px", height: "400px" }}></div>
            </Box>

            <Box>
               <Box component="form" noValidate sx={{
                  mt: 1,
                  display: 'flex', flexDirection: 'column', alignItems: 'center',
                  background: 'black', padding: '20px', borderColor: 'white',
                  borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
                  marginTop: '30px', marginBottom: '30px',
               }} onSubmit={handleSubmitString}>
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
                  <Grid item>
                     <StyleButton text={"Submit"} type={"submit"} onclick={playSound} />
                  </Grid>
                  <Snackbar open={error} autoHideDuration={3000} onClose={() => setError(false)}>
                     <Alert severity="error" sx={{ fontFamily: "Undertale" }}>
                        {errorText}
                     </Alert>
                  </Snackbar>
               </Box>
            </Box>
         </Container>
      </>
   )
}

export default MainPage;
