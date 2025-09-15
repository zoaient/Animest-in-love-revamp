import 'vuetify/styles'
import { createVuetify } from 'vuetify' 
import type { ThemeDefinition } from 'vuetify'
const myCustomDarkTheme: ThemeDefinition = {
  dark: true,
  colors: {
    background: '#121212',
    surface: '#212121',
    primary: '#BB86FC',
    secondary: '#03DAC6',
    error: '#CF6679',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
    'on-surface': '#FFFFFF',
    'on-background': '#FFFFFF',
  }
}

export default createVuetify({
  theme: {
    defaultTheme: 'myCustomDarkTheme',
    themes: {
      myCustomDarkTheme,
    }
  }
})