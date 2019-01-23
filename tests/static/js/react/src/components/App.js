import React from 'react'
import { styled } from 'reakit'
import { Query } from 'react-apollo'

import TestInfo from './TestInfo'
import { me } from '../graphql/queries'


class App extends React.Component {

  handleOnStartTest = () => {
    // eslint-disable-next-line
    console.log('handleOnStartTest')
  }

  render() {
    return (
      <Query query={me}>
        {({ loading, error, data }) => {
          console.log('**** DATA: ', { data })
          if (loading) return <p>Loading...</p>
          if (error) return <p>Error :(</p>
          return data.allTests.map((test, index) => (
            <Wrapper key={index}>
              <TestInfo test={test} me={data.me} />
            </Wrapper>
          ))
        }}
      </Query>
    )
  }
}

export default App

const Wrapper = styled.div`
  padding-bottom: 56px;
`
