import React, { useState, useEffect } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";

function VideoLinksPage({ videoList }) {

	return (
		<Container>

			{	
				videoList.map((videoLink, index) => (
				<Card key={index}>
					<Card.Body>
						<Card.Text>{videoLink.fields.video_link}</Card.Text>
					</Card.Body>
				</Card>
			))}
		</Container>
	);
}
export default VideoLinksPage;
/*videoLinks.map(function link(videoLink) {
	return (				
				<Card>
					<Card.Body>
						<Card.Text>
						{videoLink.video_link}
						</Card.Text>
					</Card.Body>
				</Card>
			)
}
)
*/
/*		async function loadVideoLinks() {
			let response = await fetch(
				"http://localhost:8000/backend/video_links"
			);
			setVideoLinks(await response.json());
		}
		loadVideoLinks()
*/
