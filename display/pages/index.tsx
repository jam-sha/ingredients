import type { NextPage } from 'next';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import React, { useState, useEffect } from 'react'

const Home: NextPage = () => {


  const [data, setData] = useState<any | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/members").then(
      res => res.text()
    ).then(
      data => {
        setData(data)
      }
    )
  }, [])

 

  return (
    <Container maxWidth="lg">
      <Box
        sx={{
          my: 4,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Typography variant="h4" component="h1" gutterBottom>
          Ingredient Analyser
        </Typography>
        <Button variant="contained" href="" color="secondary">
          Go to the about page
        </Button>
        <div>
          <li>{data}</li>
        </div>
      </Box>
    </Container>
  );
};

export default Home;
