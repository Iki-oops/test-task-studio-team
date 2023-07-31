import { useTheme } from "@emotion/react"
import { Box, Typography } from "@mui/material"
import { tokens } from "../theme";



const TeamProfile = ({ name, position, photoURL }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box
      backgroundColor={colors.primary[400]}
      display='flex'
      justifyContent='center'
      p='30px'
      sx={{flexDirection: 'column', alignItems: 'center'}}
    >
      <img
        alt='not found img'
        src={photoURL}
        width='300px'
        height='400px'
        style={{textAlign: 'center', objectFit: 'cover'}}
      />
      <Typography variant="h4" fontWeight='bold' sx={{ color: colors.grey[100], marginLeft: '10px' }}>
        {name}
      </Typography>
      <Typography variant="h5" sx={{ color: colors.greenAccent[500], marginLeft: '10px' }}>
        {position}
      </Typography>
    </Box>
  )
}

export default TeamProfile;
