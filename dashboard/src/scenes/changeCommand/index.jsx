import { Box, Button, FormHelperText, InputLabel, MenuItem, Select, TextField, Typography } from "@mui/material";
import * as yup from "yup";
import { useState } from "react";
import Header from "../../componets/Header";
import { Formik } from 'formik';
import { useTheme } from "@emotion/react";
import { tokens } from "../../theme";

const checkoutSchema = yup.object().shape({
  firstName: yup.string().required("required"),
  lastName: yup.string().required("required"),
  email: yup.string().email("invalid email").required("required"),
  contact: yup
    .string()
    .required("required"),
  address1: yup.string().required("required"),
  address2: yup.string().required("required"),
});


const ChangeCommand = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode)

  const commands = [
    '/weather', '/start', '/help', '/news'
  ]
  const [command, setCommand] = useState(commands[0]);

  const handleFormSubmit = (values) => {
    console.log(values);
  };

  return (
    <Box m="20px">
      <Header title="Поменять команду" subtitle="Здесь можете поменять текст команды" />

      <Box display='flex' justifyContent='center' alignContent='center'>
        <Formik
          onSubmit={handleFormSubmit}
          initialValues={{selectCommand: 'Выберите команду', text: ''}}
          // validationSchema={checkoutSchema}
        >
          {({
            values,
            errors,
            touched,
            handleBlur,
            handleChange,
            handleSubmit
          }) => (
            <form
              onSubmit={handleSubmit}
              style={{width: '600px', backgroundColor: `${colors.primary[400]}`, borderRadius: '5px'}}
            >
              <Box
                display="flex"
                justifyContent='center'
                alignItems='center'
                sx={{
                  flexDirection: 'column',
                  m: '30px'
                }} 
              >
                <Typography variant='h3' fontWeight='bold' sx={{ color: colors.grey[100], mb: '20px' }}>Поменять текст команды</Typography>
                <InputLabel id="select-command-label" sx={{mb: '10px'}}>Команда</InputLabel>
                <Select
                  labelId="select-command-label"
                  id="selectCommand"
                  value={command}
                  label="select-command"
                  onChange={e => setCommand(e.target.value)}
                  sx={{
                    width: '100%',
                  }}
                >
                  <MenuItem value={commands[0]}>/weather</MenuItem>
                  <MenuItem value={commands[1]}>/start</MenuItem>
                  <MenuItem value={commands[2]}>/help</MenuItem>
                  <MenuItem value={commands[3]}>/news</MenuItem>
                </Select>
                <FormHelperText sx={{mt: '10px'}}>Выберите команду</FormHelperText>

                <InputLabel id="command-text-label" sx={{mt: '40px', mb: '10px'}}>Текст команды</InputLabel>
                <TextField
                  fullWidth
                  variant="filled"
                  type="text"
                  multiline
                  rows={8}
                  label="Text"
                  onBlur={handleBlur}
                  onChange={handleChange}
                  value={values.text}
                  name="text"
                  error={!!touched.firstName && !!errors.firstName}
                />
                <FormHelperText sx={{mt: '10px'}}>sdfsdfsdf</FormHelperText>

                <Box mt="30px">
                  <Button
                    type="submit"
                    color="secondary"
                    variant="contained"
                    sx={{fontWeight: "bold", color: colors.grey[900]}}
                  >
                    Поменять команду
                  </Button>
                </Box>
              </Box>
            </form>
          )}
        </Formik>
      </Box>
    </Box>
  );
};

export default ChangeCommand;
