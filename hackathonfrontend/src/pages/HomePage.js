import { Box, Button } from "@mui/material";
import { useNavigate } from "react-router";
import { Link } from "react-router";
import { Typography } from "@mui/material/";
import logo from "../assets/pfl.png"; // Replace with your image path

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
       
      <Box
          component="img"
          src={logo}
          alt="PetrFindr Logo"
          sx={{
            width: "200%", // Set image width
            height: "auto", // Maintain aspect ratio
            marginBottom: "20px", // Add spacing below the image
            alignSelf: "center", // Center the image horizontally
          }}
        />
       
        {/* <Typography variant="h1" sx={{fontSize: "70px", paddingBottom: "20px"}}>PetrFindr</Typography> */}
        <Box sx={{display: 'flex', justifyContent: 'space-between'}}>
            <Button variant="contained" sx={{backgroundColor: 'primary.dark'}} onClick={() => {navigate('/project')}}>Find Location</Button>
            <Button variant="contained" sx={{backgroundColor: 'primary.dark'}} component={Link} to='/team-bio'>Team Bio</Button>
        </Box>
      </Box>
    </Box>
  );
}
