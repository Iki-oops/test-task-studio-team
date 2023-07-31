import { useTheme } from "@emotion/react";
import { Avatar, Divider, List, ListItem, ListItemAvatar, ListItemButton, ListItemText, Paper, Typography } from "@mui/material";
import { tokens } from "../theme";
import { useCallback, useEffect, useState } from "react";
import { useHttp } from "../hooks";


const FilterMessages = (props) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode)
  const { request } = useHttp()
  const [profiles, setProfiles] = useState([])

  useEffect(() => {
    request('http://localhost:8000/api/profiles/')
      .then(setProfiles)
      .catch(console.log)
  }, [])

  const renderProfiles = () => {

    return profiles.map(item => {
      console.log(item)
      const displayName = <Typography variant="h5">{item.profile_name}</Typography>

      return (
        <ListItem disablePadding key={item.telegram_id} width='100%'>
          <ListItemButton onClick={() => {props.setUserChat(item.telegram_id)}}>
            <ListItemAvatar>
              <Avatar alt='profile img' src={item.avatar_url} />
            </ListItemAvatar>
            <ListItemText primary={displayName} />
          </ListItemButton>
        </ListItem>
      )
    })
  }

  return (
    <Paper
      sx={{
        display: 'flex',
        backgroundColor: `${colors.primary[400]} !important`,
        position: 'relative',
        maxWidth: '300px',
        height: '300px',
        justifyContent: 'center',
        overflow: 'auto'
      }}
      display='flex'
      position='relative'
    >
      <nav aria-label="profiles filter">
        <Typography variant='h5' sx={{m: '10px', fontWeight: 700}}>Фильтр пользователей</Typography>
        <Divider />
        <List>  
          {renderProfiles()}
        </List>
      </nav>
    </Paper>
  )
}

export default FilterMessages;
