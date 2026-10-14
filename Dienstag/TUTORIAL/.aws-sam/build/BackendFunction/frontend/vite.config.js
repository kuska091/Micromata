import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/login': 'http://127.0.0.1:5000',
      '/register': 'http://127.0.0.1:5000',
      '/logout': 'http://127.0.0.1:5000',
      '/pakete': 'http://127.0.0.1:5000',
      '/autoarten': 'http://127.0.0.1:5000',
      '/kunden': 'http://127.0.0.1:5000',
      '/belegt': 'http://127.0.0.1:5000',
      '/detailing_factory': 'http://127.0.0.1:5000',
    },
  },
})