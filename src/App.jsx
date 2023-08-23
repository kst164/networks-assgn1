import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ForceGraph2D from 'react-force-graph-2d';

function App() {
  const [count, setCount] = useState(0)
  const [data, setData] = useState(null)
  useEffect(() => {
    fetch('data.json').then(res => res.json()).then(data => {
      console.log(data);
      setData(data);
    })
  }, [])
  return (
    <>
      <div>
        {data && (
          <ForceGraph2D
            graphData={data}
            nodeLabel="id"
            nodeAutoColorBy="group"
            linkDirectionalParticles="value"
            linkDirectionalParticleSpeed={d => d.value * 0.001}
          />
        )}
      </div>
    </>
  )
}

export default App
