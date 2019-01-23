import React from 'react'
import { render } from 'react-dom'
import theme from 'reakit-theme-default'
import { Provider } from 'reakit'

import ApolloClient from 'apollo-boost'
import Cookies from 'js-cookie'
import { ApolloProvider } from 'react-apollo'


import App from './components/App'
// import Store from './models/Store'


const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/',
  headers: {
    'X-CSRFToken': Cookies.get('csrftoken'),
  }
})


render(
  <ApolloProvider client={client}>
    <Provider theme={theme}>
      <App />
    </Provider>
  </ApolloProvider>,
  document.getElementById('react')
)
