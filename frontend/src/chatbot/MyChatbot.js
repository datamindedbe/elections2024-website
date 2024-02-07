// MyChatbot.js
import React from 'react';
import Chatbot from 'react-chatbot-kit';
import config from './config.js';
import MessageParser from './MessageParser.jsx';
import ActionProvider from './ActionProvider.jsx';
import 'react-chatbot-kit/build/main.css'
import './MyChatbot.css';
import { useGoogleLogin } from '@react-oauth/google';



const MyChatbot = () => {
    const login = useGoogleLogin({
        onSuccess: tokenResponse => console.log(tokenResponse),
        // Configure additional options as needed
    });

    return (
        <div className='floating-chatbot'>
            <button onClick={() => login()}>Login with Google</button>
            {/* Render Chatbot or other components based on login status */}
        </div>
    );
};
