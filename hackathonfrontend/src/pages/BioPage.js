import { Box, Grid2, Card, CardContent, Button } from "@mui/material";
import BioCard from "../components/BioCard";
import blo from "../assets/blo.jpg";
import qian from "../assets/ying.jpg";
import justin from "../assets/justin.png";
import bh from "../assets/bhj.jpg";
import { Typography } from "@mui/material/";
import { useNavigate } from "react-router";
import { Link } from "react-router";

export default function BioPage() {
  const names = ["Brandon L", "Justin", "Ying", "Brandon H"];
  const teamInfo = [
    {
      pic: blo,
      name: "Brandon Lo",
      age: 20,
      major: "Informatics",
      info: "Passionate about frontend design, specializing in creating intuitive and visually appealing UI/UX interfaces for applications that enhance user experiences and meet functional goals.",
    },
    {
      pic: qian,
      name: "Ying Wong",
      age: 22,
      major: "Cognitive Sciences",
      info: "My strong interest in project management is reflected in my ability to thrive in collaborative environments. My goal is to build a career as an AI solutions architect in the game industry, merging my expertise in AI with my passion for gaming while continuing to develop my project management skills in dynamic team settings.",
    },
    {
      pic: justin,
      name: "Justin Lo",
      age: 19,
      major: "Computer Engineering",
      info: "I am ambitious in my studies of physical and electrical components of computers. I'm looking forwards to building my skills as a hardware engineer by learning how to create and integrate software within my projects.",
    },
    {
      pic: bh,
      name: "Brandon Huynh",
      age: 21,
      major: "Computer Science",
      info: "I have extensive programming experience in machine learning projects and have worked on several large-scale projects on cross-functional teams involving designers and product-managers in AGILE environments.",
    },
  ];
  return (
    <Box
      sx={{
        width: "100vw",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        backgroundColor: "lightblue", // Change background color here
      }}
    >
      
      <Typography variant="h1" sx={{fontSize: "30px", paddingTop: "2%", paddingLeft: "2%", paddingBottom: "2%"}}>About Us</Typography>
      
      <Grid2
        container
        spacing={4}
        // sx={{
        //   display: "flex",
        //   justifyContent: "center",
        //   alignItems: "center", // Center items vertically
        //   flexWrap: "wrap",
        // }}
      >
        {teamInfo.map((teamMember) => {
          return (
            <>
              <Grid2
                sx={{ display: "flex", justifyContent: "center" }}
                size={6}
              >
                <BioCard nameOfPerson={teamMember} />
              </Grid2>
            </>
          );
        })}
      </Grid2>
    </Box>
  );
}
