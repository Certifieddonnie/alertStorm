import './globals.css'
import { Inter } from 'next/font/google'
import { RegisterPWA } from "./register";

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="manifest" href="/manifest.json" />
        <link rel="apple-touch-icon" href="/icon.png"></link>
        <meta name="theme-color" content="#fff" />
      </head>
      <body className={inter.className}>
      {children}
      <RegisterPWA />
      </body>
    </html>
  )
}
