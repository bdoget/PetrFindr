import createTheme from '@mui/material/styles/createTheme';

const colorTheme = createTheme({
  palette: {
    primary: {
      main: '#41e2ba',
      light: '#A9E2D4',
      dark: '#1D6654',
      contrastText: '#E5FFF9'
    },
    secondary: {
      main: '#e0bad7',
    },
    info: {
      main: '#e0bad7',
    },
    error: {
      main: '#e5625e',
    },
    success: {
      main: '#61d095',
    },
  },
});

const theme = createTheme(colorTheme, {
  components: {

  }
});

export default theme;