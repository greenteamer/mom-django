import { styled, Button } from 'reakit'


const MyButton = styled(Button)`
  background-color: #3477bb;
  box-shadow: 0px 2px 32px 0px rgba(4, 123, 248, 0.3);
  transition: all ease 0.3s;
  &:hover {
    background-color: #23527c;
  }
`
export default MyButton