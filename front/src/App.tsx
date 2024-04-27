import * as React from 'react';
import List from '@mui/material/List';
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import Paper from '@mui/material/Paper';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import AccessibleForwardIcon from '@mui/icons-material/AccessibleForward';
import AssistWalkerIcon from '@mui/icons-material/AssistWalker';
import BlindIcon from '@mui/icons-material/Blind';

import {
  Link as RouterLink,
  LinkProps as RouterLinkProps,
  Route,
  Routes,
  MemoryRouter,
  useLocation,
} from 'react-router-dom';
import { StaticRouter } from 'react-router-dom/server';
import { Grid, Typography } from '@mui/material';
import Lab6 from './pages/Lab6.tsx'
import Lab5 from './pages/Lab5.tsx'
import Lab4 from './pages/Lab4.tsx'
import Error from './pages/Error.tsx'


function Router(props: { children?: React.ReactNode }) {
  const { children } = props;
  if (typeof window === 'undefined') {
    return <StaticRouter location="/error">{children}</StaticRouter>;
  }

  return (
    <MemoryRouter initialEntries={['/app']} initialIndex={0}>
      {children}
    </MemoryRouter>
  );
}

interface ListItemLinkProps {
  icon?: React.ReactElement;
  primary: string;
  to: string;
}

const Link = React.forwardRef<HTMLAnchorElement, RouterLinkProps>(
  function Link(itemProps, ref) {
    return <RouterLink ref={ref} {...itemProps} role={undefined} />;
  },
);

function ListItemLink(props: ListItemLinkProps) {
  const { icon, primary, to } = props;

  return (
    <li>
      <ListItem button component={Link} to={to}>
        {icon ? <ListItemIcon>{icon}</ListItemIcon> : null}
        <ListItemText primary={primary} />
      </ListItem>
    </li>
  );
}

function Content() {
  const location = useLocation();
  return (
    <Typography variant="body2" sx={{ pb: 2 }} color="text.secondary">
      Current route: {location.pathname}
    </Typography>
  );
}
function App() {

  const switchTabs = new Audio('src/assets/sounds/switch_tabs.mp3');
  const switchPlay = () => {
    switchTabs.play();
  }

  return (
    <Router>
      <Box sx={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <Paper elevation={0} >
          <List aria-label="main sections" sx={{
            color: 'white',
            backgroundColor: 'black',
            display: 'flex',
            flexDirection: 'row',
            justifyContent: 'center',
            alignItems: 'center',
            scale: "130%"
          }}>
            <ListItemLink to="/lab4" primary="Lab4" icon={<BlindIcon color='primary' />} />
            <ListItemLink to="/lab5" primary="Lab5" icon={<AccessibleForwardIcon color='primary' />} />
            <ListItemLink to="/lab6" primary="Lab6" icon={<AssistWalkerIcon color='primary' />} />
          </List>
        </Paper>
      </Box>
      <Grid container maxWidth={'xs'}>
        <Grid item sx={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <Routes>
            <Route path="/lab4" element={<Lab4 />} />
            <Route path="/lab5" element={<Lab5 />} />
            <Route path="/lab6" element={<Lab6 />} />
          </Routes>
        </Grid>
        <Grid item sx={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <Routes>
            <Route path="/error" element={<Error />} />
          </Routes>
        </Grid>
      </Grid>
    </Router>
  )
}

export default App;
