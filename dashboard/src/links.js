import MessageOutlinedIcon from '@mui/icons-material/MessageOutlined';
import FormatListBulletedOutlinedIcon from '@mui/icons-material/FormatListBulletedOutlined';
import PeopleOutlinedIcon from '@mui/icons-material/PeopleOutlined';
import ContactsOutlinedIcon from '@mui/icons-material/ContactsOutlined';
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined';


export const urlLinks = {
  data: {
    title: 'Информация',
    links: [
      {
        aboutTeam: {
          title: 'О команде',
          icon: <PeopleOutlinedIcon />,
          to: '/about-team',
          isAdmin: false,
        },
        contact: {
          title: 'Контакты',
          icon: <ContactsOutlinedIcon />,
          to: '/contacts',
          isAdmin: false,
        }
      }
    ]
  },
  pages: {
    title: 'Страницы',
    links: [
      {
        historyMessages: {
          title: 'History of Messages',
          icon: <MessageOutlinedIcon />,
          to: '/',
          isAdmin: false,
        },
        changeForm: {
          title: 'Change Form',
          icon: <FormatListBulletedOutlinedIcon />,
          to: '/change-form',
          isAdmin: true,
        },
        dashboard: {
            title: 'Dashboard',
            icon: <HomeOutlinedIcon />,
            to: '/dashboard',
            isAdmin: true,
        }
      }
    ],
  }
}

