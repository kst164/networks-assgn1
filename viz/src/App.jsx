import { useState, useEffect, useRef } from 'react'
import './App.css'
import ForceGraph2D from 'react-force-graph-2d';
import ForceGraph3D from 'react-force-graph-3d';
function App() {
  const [data, setData] = useState(null)
  const graphRef = useRef(null);

  useEffect(() => {
    fetch('data.json').then(res => res.json()).then(data => {
      console.log(data);
      setData(data);
    })
  }, [])
  // useEffect(() => {
  //   if (data) {
  //     graphRef.current.d3Force('link').distance(
  //       d => d.value * 100
  //     )
  //   }
  // }, [data])
  const speedFactor = 0.001;

  const colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'orange',
    6: 'purple',
    7: 'pink',
    8: 'brown',
    9: 'grey',
    10: 'purple',
  }


  return (
    <>
      <div>
        {data && (
          <>
          <ForceGraph2D
            graphData={data}
            nodeLabel="id"
            nodeAutoColorBy="group"
            linkDirectionalParticles="value"
            linkDirectionalParticleSpeed={d => (d.value + d.value*(Math.random()*0.2 - 0.1)) * speedFactor}
            linkDirectionalParticleColor={d=> colors[d.color]}
            linkLabel={d => d.label}
            ref={graphRef}
            // linkDirectionalArrowLength={d => d.value * 2}
            // linkCurvature={0.1}
          />
          {/* <ForceGraph3D
            graphData={data}
            nodeLabel="id"
            nodeAutoColorBy="group"
            linkDirectionalParticles="value"
            linkDirectionalParticleSpeed={d => (d.value + d.value*(Math.random()*0.2 - 0.1)) * speedFactor}
            linkDirectionalParticleWidth={4}
            linkDirectionalParticleColor={d => colors[d.value]}
            linkLabel={d => d.value}
            ref={graphRef}
            // linkDirectionalArrowLength={d => d.value * 2}
            // linkAutoColorBy={d => colors[d.value]}
            // linkCurvature={0.1}
            /> */}
          </>
        )}
      </div>
    </>
  )
}

export default App
