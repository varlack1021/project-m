import React, { useState, useEffect } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import VideoLinksPage from "./videoLinkePage";

//takes input for GET request args
//how to pass form data to func?

function App() {
  //useState returns variable and setter function
  //anytime the func is called itll update the variable
  let [formData, setFormData] = useState({  video_link: ""  });
  let [videoList, setVideoList] = useState([]);

  // 1) initialize form data to be empty
  // 2) initialize our list of videolinks to be empty
  // 3) when the page is ready to show, load all video
  //    links into our array
  // 4) add a new video link, hit submit
  //      a) send that video link to the server to be saved in the db
  //      b) push that new video link object in the form into our array in the browser
  // 5) pass the array of video links into the video links page component


  //the response looks like {model :"", fields:""}
  
  //waits to load things based on what we want it to wait on,
  //if we give it empty list then it does things when the page loads
  useEffect(() => {

    fetch("http://localhost:8000/backend/video_links").then((response) => {
      return response.json().then((json) => setVideoList(json));
    });
  }, []);

  const saveVideo = async (formEvent) => {
    formEvent.preventDefault();

    const requestOptions = {
      method: "POST",

      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    };

    let response = await fetch(
      "http://localhost:8000/backend/createVideoLink/",
      requestOptions
    );

    response = await response.json();

    setVideoList([{ fields: response }, ...videoList]);
    setFormData({ video_link: "" } );

  };

  return (
    <Container>
      {/*mt, margin-top 5 outside of component*/}
      <Form className="mt-5" onSubmit={(formEvent) => saveVideo(formEvent)}>
        <Form.Group>
          <Form.Label>Video Link</Form.Label>

          <Form.Control
            type="url"
            placeholder="Enter video link"
            onChange={(inputEvent) =>
              setFormData({ ...formData, video_link: inputEvent.target.value })
            }
            value={formData.video_link}
          />
          <Form.Text className="text-muted">
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
      { //videoList.map((video, index) => (
        //   <div key={index}>{video.video_link}</div>
        //  ))
      }
      <VideoLinksPage videoList={videoList} />
    </Container>
  );
}

export default App;
