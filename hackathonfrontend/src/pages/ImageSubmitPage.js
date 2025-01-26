import { Box, Button } from "@mui/material";
import { useState } from "react";
import { sendImageToServer } from "../routes/imageTransport";

export default function ImageSubmitPage() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [location, setLocation] = useState('')
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
          onChange={async (event) => {       
            setSelectedImage(event.target.files[0]); // Update the state with the selected file
            // const formData = new FormData();
            // formData.append("image", event.target.files[0]);
            // const detectedLocation = await sendImageToServer(formData);
            // setLocation(detectedLocation);
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
          {location && (
            <h1>{location}</h1>
          )}
          <br /> <br />
          {/* Button to remove the selected image */}
          <button onClick={() => setSelectedImage(null)}>Remove</button>
        </div>
      )}
    </Box>
  );
}
