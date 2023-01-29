import logo from './logo.svg';
import './App.css';

import React, { useState, useRef } from 'react';
import Webcam from 'react-webcam';

const CameraManager = () => {
        const [activeCameraIndex, setActiveCameraIndex] = useState(0);
        const [cameras, setCameras] = useState([
            { id: 1, name: 'Camera 1' },
            { id: 2, name: 'Camera 2' },
            { id: 3, name: 'Camera 3' },
            // Add more cameras here as needed
        ]);
        const [imageSrc, setImageSrc] = useState(null);
        const [isRecording, setIsRecording] = useState(false);
        const [motionDetected, setMotionDetected] = useState(false);
        const webcamRefs = useRef([]);

        const handleTakePhoto = () => {
            const imageSrc = webcamRefs.current[activeCameraIndex].getScreenshot();
            setImageSrc(imageSrc);
        };

        const handleStartRecording = () => {
            setIsRecording(true);
            // Code to start recording the video here
        };

        const handleStopRecording = () => {
            setIsRecording(false);
            // Code to stop recording the video here
        };

        const handleMotionDetection = () => {
            // Code to detect motion here
            setMotionDetected(true);
        };

        const handleCameraChange = (index) => {
            setActiveCameraIndex(index);
        };

        return ( <
            div >
            <
            div > {
                cameras.map((camera, index) => ( <
                    button key = { camera.id }
                    onClick = {
                        () => handleCameraChange(index) } > { camera.name } <
                    /button>
                ))
            } <
            /div> <
            Webcam audio = { false }
            height = { 500 }
            ref = {
                (webcamRef) => {
                    webcamRefs.current[activeCameraIndex] = webcamRef;
                }
            }
            screenshotFormat = "image/jpeg"
            width = { 500 }
            /> <
            div >
            <
            button onClick = { handleTakePhoto } > Take Photo < /button> { imageSrc && < img src = { imageSrc }
                alt = "Captured" / > } <
            /div> <
            div > {!isRecording ? ( <
                    button onClick = { handleStartRecording } > Start Recording < /button>
                ) : ( <
                    button onClick = { handleStopRecording } > Stop Recording < /button>
                )
            } <
            /div> <
            div > {
                motionDetected && < p > Motion detected! < /p>} <
                button onClick = { handleMotionDetection } > Start Motion Detection < /button> <
                /div> <
                /div>
            );
        };

        export default CameraManager;