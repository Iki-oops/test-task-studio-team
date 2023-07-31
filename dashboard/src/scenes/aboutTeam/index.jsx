import { Box } from "@mui/material"
import Header from "../../componets/Header"
import TeamProfile from "../../componets/TeamProfile";

const AboutTeam = () => {

  return (
    <Box m='20px'>
      <Header title='О нас' subtitle='Добро пожаловать на страницу с информацией о нашей команде' />
      <Box display='flex' justifyContent='space-around'>
        <TeamProfile
          name='Илон Маск'
          position='Старший помощник'
          photoURL="https://i.ibb.co/82WgqP8/Elon-Musk-Royal-Society-crop2.jpg"
        />
        <TeamProfile
          name='Бамбагаев Дмитрий'
          position='Президент'
          photoURL="https://i.ibb.co/7gYVbtm/photo-2023-07-12-22-43-06.jpg"
        />
        <TeamProfile
          name='Марк Цукерберг'
          position='Программист HTML, CSS'
          photoURL="https://i.ibb.co/T0Zswy3/Mark-Zuckerberg-F8-2019-Keynote-32830578717-cropped.jpg"
        />
      </Box>
    </Box>
  )
}

export default AboutTeam;
