import { Box, useTheme } from "@mui/material";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { tokens } from "../../theme";
import Header from "../../componets/Header";

const FAQ = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
    <Box m="20px">
      <Header title="FAQ" subtitle="Часто задаваемы вопросы" />

      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            Как я могу создать аккаунт на Dashboard сайте?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Чтобы создать аккаунт на Dashboard сайте, нажмите на ссылку в правом верхнем углу "Sign up". 
            Заполните необходимые поля в форме регистрации и нажмите кнопку "Создать аккаунт"
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            Как я могу войти в свой аккаунт на Dashboard сайте?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Чтобы войти в свой аккаунт, нажмите на ссылку в правом верхнем углу "Login".
            Введите свои учетные данные, такие как электронная почта и пароль, и нажмите кнопку "Войти".
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            Как я могу связаться с поддержкой Dashboard сайта?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Чтобы связаться с поддержкой Dashboard сайта, перейдите на страницу "Поддержка" 
            и заполните форму обратной связи. Нажмите кнопку "Отправить" для отправки сообщения в службу поддержки.
          </Typography>
        </AccordionDetails>
      </Accordion>
    </Box>
  );
};

export default FAQ;
