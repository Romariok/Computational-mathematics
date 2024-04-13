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

interface Rows {
   x: string;
   y: string;
   r: string;
}

function MainPage(): JSX.Element {
   const [openError, setOpenError] = useState<boolean>(false);

   const ring = new Audio('src/assets/sounds/ring.mp3');

   const playSound = () => {
      ring.play();
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


            <Box>
               <Box component="form" noValidate sx={{
                  mt: 1,
                  display: 'flex', flexDirection: 'column', alignItems: 'center',
                  background: 'black', padding: '20px', borderColor: 'white',
                  borderWidth: '6px', textAlign: 'center', borderStyle: 'solid',
                  marginTop: '30px', marginBottom: '30px',
               }}>
                  <Box id='x'>
                     <Grid container>
                     </Grid>
                  </Box>
                  
                  <Input
                     margin="dense"
                     required
                     fullWidth
                     id="y"
                     name="y"
                     autoComplete="y"
                     autoFocus
                     sx={{ color: 'white' }}
                     inputProps={{ min: -5, max: 5 }}
                     placeholder='Y'
                     type='number'
                  />
                  <Box id='r'>
                     <Grid container>
                        {/* Grid items */}
                     </Grid>
                  </Box>
                  <Grid container>
                     <Grid item sx={{ ml: 5 }}>
                        <StyleButton text={"Submit"} type={"button"} />
                     </Grid>
                     <Grid item sx={{ ml: 13 }}>
                        <StyleButton text={"Clear"} type={"button"} />
                     </Grid>
                  </Grid>
                  <Snackbar open={openError} autoHideDuration={3000} onClose={() => setOpenError(false)}>
                     <Alert severity="error" sx={{ fontFamily: "Undertale" }}>
                        {/* {errorMessage} */}
                     </Alert>
                  </Snackbar>
               </Box>
            </Box>
         </Container>
      </>
   )
}

export default MainPage;
