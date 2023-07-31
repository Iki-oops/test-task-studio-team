import { Box, Button } from "@mui/material";
import Header from "../../componets/Header";
import BarChart from "../../componets/BarChart";
import { useTheme } from "@emotion/react";
import { tokens } from "../../theme";
import StatBox from "../../componets/StatBox";
import PersonOutlinedIcon from '@mui/icons-material/PersonOutlined';
import BackupOutlinedIcon from '@mui/icons-material/BackupOutlined';
import ChecklistOutlinedIcon from '@mui/icons-material/ChecklistOutlined';
import ChatOutlinedIcon from '@mui/icons-material/ChatOutlined';
import { useHttp } from "../../hooks";
import { useEffect, useState } from "react";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const { request } = useHttp();
  const [ data, setData ] = useState([]);

  useEffect(() => {
    request('http://localhost:8000/api/messages/statistics/')
      .then(setData)
      .catch(console.log)
  }, [])

  const iconStyle = {color: colors.greenAccent[600], fontSize: '26px'}

  return (
    <Box m='20px'>
      <Header title='Dashboard' subtitle='Добро пожаловать на дашборд' />
      <Box display='flex' justifyContent='space-between'>
        <Box backgroundColor={colors.primary[400]} display='flex' justifyContent='center' maxWidth='350px'>
          <StatBox
            title={data.new_users ? data.new_users : 'Нет данных'}
            subtitle='Новых пользователей'
            icon={<PersonOutlinedIcon sx={iconStyle} />}
          />
        </Box>
        <Box backgroundColor={colors.primary[400]} display='flex' justifyContent='center' maxWidth='350px'>
          <StatBox
            title={data.active_dialogues ? data.active_dialogues : 'Нет данных'}
            subtitle='Активных диалогов'
            icon={<ChecklistOutlinedIcon sx={iconStyle} />}
          />
        </Box>
        <Box backgroundColor={colors.primary[400]} display='flex' justifyContent='center' maxWidth='350px'>
          <StatBox
            title={data.queries ? data.queries : 'Нет данных'}
            subtitle='Запросов за неделю'
            icon={<BackupOutlinedIcon sx={iconStyle} />}
          />
        </Box>
        <Box backgroundColor={colors.primary[400]} display='flex' justifyContent='center' maxWidth='350px'>
          <StatBox
            title={data.popular_command ? data.popular_command : 'Нет данных'}
            subtitle='Популярная команда'
            icon={<ChatOutlinedIcon sx={iconStyle} />}
          />
        </Box>
      </Box>
      <Box height='500px'>
        <BarChart />
      </Box>
    </Box>
    
  )
}

export default Dashboard;
