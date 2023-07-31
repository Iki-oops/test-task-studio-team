import React from "react";
import { Avatar, Box } from "@mui/material";

import './Message.scss';


export const MessageLeft = (props) => {
  const message = props.message ? props.message : "no message";
  const timestamp = props.timestamp ? props.timestamp : "DD.MM HH:MM";
  const avatarURL = props.avatarURL ? props.avatarURL : "https://i.ibb.co/BNv3Pxy/image-not-found.jpg";
  const displayName = props.displayName ? props.displayName : "Anonymous";

  return (
    <Box className='message-row'>
      <Avatar alt="Remy Sharp" src={avatarURL} />
      <Box>
        <Box className='display-name'>{displayName}</Box>
        <Box className='message-user'>
          <Box>
            <p className='message-content'>{message}</p>
          </Box>
          <Box className='message-timestamp-right'>{timestamp}</Box>
        </Box>
      </Box>
    </Box>
  );
};

export const MessageRight = (props) => {
  const message = props.message ? props.message : "no message";
  const timestamp = props.timestamp ? props.timestamp : "DD.MM HH:MM";
  const imgUrl = props.imgUrl ? props.imgUrl : null

  return (
    <Box className='message-row__right'>
      <Box display='flex' flexWrap='wrap-reverse' flexDirection='column'>
        <Box className='display-name' display='flex' justifyContent='end' mr='10px'>Sky Guardian☁️</Box>
          <Box className='message-bot'>
            {
              imgUrl ?
              <img
                alt='not found img'
                src={imgUrl}
                width='300px'
                height='300px'
                style={{textAlign: 'center', objectFit: 'cover'}}
              /> :
              null
            }
            <p className='message-content'>{message}</p>
          <Box className='message-timestamp-right'>{timestamp}</Box>
        </Box>
      </Box>
      <Avatar alt="Remy Sharp" src='https://i.ibb.co/jh2Z9Qt/3a10f5b2e3152efe1b5d73feafbc4dad.jpg' />
    </Box>
  );
};
