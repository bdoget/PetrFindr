import { Box, Button } from "@mui/material";
import { useNavigate } from "react-router";
import { Link } from "react-router";
import { Typography } from "@mui/material/";

export default function HomePage() {
    let navigate = useNavigate();

  return (
    <Box
      sx={{
        width: "100vw",
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "lightblue", 
      }}
    >
      <Box sx={{ display: "flex", flexDirection: "column", width: '20%', textAlign: 'center'}}>  
        <Typography variant="h1" sx={{fontSize: "60px", paddingBottom: "20px"}}>PetrFindr</Typography>
        <Box sx={{display: 'flex', justifyContent: 'space-between'}}>
            <Button variant="contained" sx={{backgroundColor: 'primary.dark'}} onClick={() => {navigate('/project')}}>Go to Project</Button>
            <Button variant="contained" component={Link} to='/team-bio'>Team Bio</Button>
        </Box>
      </Box>
    </Box>
  );
}
