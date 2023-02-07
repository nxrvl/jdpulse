import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import {ChakraProvider, Box} from '@chakra-ui/react'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'


function App({ Component, pageProps }: AppProps) {
  return (
      <ChakraProvider>
          <Navbar />
          <Box
              display="flex"
              flexDirection="column"
              minHeight="100vh"
          >
            <Component {...pageProps} />
            <Footer />
          </Box>
      </ChakraProvider>)
}

export default App