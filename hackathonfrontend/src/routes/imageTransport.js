import axios from "axios";

const BE_URL = process.env.SERVER_BE_URL;
const BE_PORT = process.env.SERVER_BE_PORT;
const BASE_URL = `${BE_URL}:${BE_PORT}`;
// const url = `${BASE_URL}/process-image`;
const url = 'http://localhost:5000/process-image'

export const sendImageToServer = async (payload) => {
  return new Promise((resolve, reject) => {
    axios
      .post(url, payload)
      .then((response) => {
        console.log('response', response);
        resolve(response.data.message);
      })
      .catch((err) => reject(`Failed to send image ${err}`));
  });
};
