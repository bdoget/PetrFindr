import { Card, CardContent, CardMedia, Typography } from "@mui/material/";
// import pikachu from "../assets/pikachu.png";
export default function BioCard({ nameOfPerson }) {
  return (
    <>
      <Card sx={{ maxHeight: "auto", height: "100%", width: "50%", border: "1px solid black", borderRadius: "8px"}} elevation={12}>
        <CardMedia
          component="img"
          height="300"
          image={nameOfPerson.pic}
          alt="bruh"
        />
        <CardContent>
          <h1>{nameOfPerson.name}</h1>
          <Typography variant="h5">Age: {nameOfPerson.age}</Typography>
          <Typography variant="h5">Major: {nameOfPerson.major}</Typography>
          <Typography variant="subtitle1">{nameOfPerson.info}</Typography>
        </CardContent>
      </Card>
    </>
  );
}
