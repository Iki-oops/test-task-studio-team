import { Box, Paper, Typography } from "@mui/material"
import Header from "../../componets/Header"
import { useTheme } from "@emotion/react"
import { tokens } from '../../theme';
import { MessageRight, MessageLeft } from "../../componets/Message";
import { useEffect, useState } from "react";
import { useHttp } from "../../hooks";
import FilterMessages from "../../componets/FilterMessages";


const HistoryMessages = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const { request } = useHttp()
  const [messages, setMessages] = useState([]);
  const [userChat, setUserChat] = useState(null);

  useEffect(() => {
    let params = '';
  
    if (userChat) {
      params = `user=${userChat}`;
    }
  
    request(`http://localhost:8000/api/messages?${params}`)
      .then(setMessages)
      .catch(err => console.log(err));
  }, [userChat])

  const renderMessages = () => {
    return messages.map((item) => {
      const userMessage = (
        <MessageLeft
          message={item.message.text}
          displayName={item.message.from_user.profile_name}
          timestamp={item.message.created_at}
          avatarURL={item.message.from_user.avatar_url}
        />
      )
      const botMessage = (
        item.response ?
        <MessageRight
          message={item.response.text}
          timestamp={item.response.created_at}
          imgUrl={item.response.photo_url}
        /> :
        undefined
        )

      return (
        <Box key={item.message.message_id}>
          {userMessage}
          {botMessage}
        </Box>
      )
    })
  }

  const content = messages.length > 0 ? renderMessages() : <MessageNotFound />

  return (
    <Box m='20px'>
      <Header title='История сообщений' subtitle='Добро пожаловать в историю сообщений пользотелей и бота' />
      <Box display='flex' justifyContent='center' >
        <Paper
          sx={{
            display: 'flex',
            backgroundColor: `${colors.primary[400]} !important`,
            position: 'relative',
            width: '800px',
            height: '580px',
            justifyContent: 'center',
            overflow: 'auto',
            mr: '30px',
          }}
          display='flex'
          position='relative'
        >
          <Box m='30px'>
            {content}
          </Box>
        </Paper>
        <Box>
          <FilterMessages setUserChat={setUserChat} />
        </Box>
      </Box>
    </Box>
  )
}

const MessageNotFound = () => {

  return (
    <Box display='flex' justifyContent='center' alignItems='center'>
      <Typography variant="h5">Messages Not Found</Typography>
    </Box>
  )
}

export default HistoryMessages;
