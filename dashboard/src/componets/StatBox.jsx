import { useTheme } from "@emotion/react"
import { Box, Typography } from "@mui/material"
import { tokens } from "../theme"

const StatBox = ({ title, subtitle, icon }) => {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode)

  return (
    <Box width="100%" m='30px 20px'>
      <Box display="flex" justifyContent="center" alignItems='center'>
        {icon}
        <Typography variant="h4" fontWeight='bold' sx={{ color: colors.grey[100], marginLeft: '10px' }}>
          {title}
        </Typography>
        <Typography variant="h5" sx={{ color: colors.greenAccent[500], marginLeft: '10px' }}>
          {subtitle}
        </Typography>
      </Box>
    </Box>
  )
}

export default StatBox;
