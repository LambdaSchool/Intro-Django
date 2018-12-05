import React, { Component } from 'react'
import styled from 'styled-components'
import axios from 'axios'
import logo from './logo.svg'
import Login from './components/Login'
import Home from './components/Home'
class App extends Component {
  state = {
    isLoggedIn: false,
    countries: []
  }

  componentDidMount() {
    const token = localStorage.getItem('token')
    if (token) {
      this.setState({ isLoggedIn: true })
    }
  }

  login = (username, password) => {
    axios.post('http://127.0.0.1:8000/api-token-auth/', { username, password })
      .then(resp => {
        localStorage.setItem('token', resp.data.token)
        this.setState({ isLoggedIn: true })
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  getData = () => {
    const token = localStorage.getItem('token')
    axios.get('http://127.0.0.1:8000/api/countries/', { headers: { Authorization: `Token ${token}` } })
      .then(resp => this.setState({ countries: resp.data }))
  }

  logout = (e) => {
    e.preventDefault()
    localStorage.clear()
    this.setState({
      isLoggedIn: false,
      countries: []
    })
  }

  render() {
    return (
      <Div1>
        <Img1 src={logo} alt="logo" />
        {
          this.state.isLoggedIn ? (
            <>
              <Button1 onClick={e => this.logout(e)}> Logout</Button1>
              <Home
                getData={this.getData}
                countries={this.state.countries}
              />
            </>
          ) : (
              <Login login={this.login} />
            )
        }
      </Div1>
    )
  }
}

const Div1 = styled.div`
            background-color: #282c34;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
          `

const Img1 = styled.img`
            animation: App-logo-spin1 infinite 30s linear;
            height: 20vmin;
          
  @keyframes App-logo-spin1 {
    from {
      transform: rotate(360deg);
    }
    to {
        transform: rotate(0deg);
    }
  }
`
const Button1 = styled.button`
  width: 100px;
  margin: 1rem auto;
  background: #61DAFB;
  padding: 5px;
  font-size: 16px;
  border-radius: 2px;
  border: none;
  box-shadow: 0 2px 2px gray;
  &:hover {
    cursor: pointer;
  }
`
export default App;
