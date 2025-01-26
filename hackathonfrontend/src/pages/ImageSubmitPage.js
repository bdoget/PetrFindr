import { Box, Button } from "@mui/material";
import { useState } from "react";

export default function ImageSubmitPage() {
  const [selectedImage, setSelectedImage] = useState(null);
  return (
    <Box
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1>Location Finder</h1>
      <Button
        variant="contained"
        component="label"
        sx={{ backgroundColor: "primary.dark" }}
      >
        Upload Image
        <input
          type="file"
          hidden
          onChange={(event) => {
            console.log(event)
            console.log(event.target.files[0]); // Log the selected file
            setSelectedImage(event.target.files[0]); // Update the state with the selected file
          }}
        />
      </Button>
      {selectedImage && (
        <div>
          {/* Display the selected image */}
          <img
            alt="not found"
            width={"250px"}
            src={URL.createObjectURL(selectedImage)}
          />
          <br /> <br />
          {/* Button to remove the selected image */}
          <button onClick={() => setSelectedImage(null)}>Remove</button>
        </div>
      )}
    </Box>
  );
}
