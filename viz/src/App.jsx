import { useState, useEffect, useRef } from 'react'
import './App.css'
import ForceGraph3D from 'react-force-graph-3d';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

import { as_info } from '../as_info';
import data from '../data.json';
const Sources = ["59193", "141340", "132780","132423","1"]
const Sinks = ["32", "54113","786","209242","13335","4538","559","1124","54113","15318","132524","132423","8075","132780","55847","141340","55479","59193","36982","28571","2200","4694","54113","9829"]
const colors = {
  0: '#6dde8b',
  1: '#2aed0c',
  2: '#de120b',
  3: '#e0a780',
  4: '#4f270d',
  5: '#e8b707',
  6: '#9cf00c',
  7: '#0c4703',
  8: '#a5f099',
  9: '#05ede5',
  10: '#35a19d',
  11: '#0aaff0',
  12: '#044159',
  13: '#e3e0e0',
  14: '#0b50e3',
  15: '#b99fe3',
  16: '#8339fa',
  17: '#29085e',
  18: '#514e54',
  19: '#e60bdb',
  20: '#eb9be7',
  21: '#ebde9b',
  22: '#ebd39b',
}

function App() {
  // const [data, setData] = useState(null)
  // const [asn, setAsn] = useState(null)
  const graphRef = useRef(null);

  // useEffect(() => {
  //   fetch('data.json').then(res => res.json()).then(data => {
  //     setData(data);
  //   })
  //   fetch('as_info.json').then(res => res.json()).then(data => {
  //     setAsn(data);
  //   })
  // }, [])

  useEffect(() => {
    if (data) {
      graphRef?.current?.d3Force('link').distance(
        100
      )
      graphRef?.current?.d3Force('charge').strength(
        -100
      )
    }
  }, [data])

  const speedFactor = 0.001;
  const [origin, setOrigin] = useState("")
  const [sink, setSink] = useState("")
  
  useEffect(() => {
    console.log(origin, sink);
  }, [origin, sink])
  
  


  return (
    <Box>
      <Box sx={{ display:"flex", flexDirection:"row", gap:"2rem", justifyContent:"center", padding:"2rem" }}>
      <FormControl sx={{width: "15rem"}}>
        <InputLabel id="demo-simple-select-label">Source</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={origin}
          label="Source"
          onChange={e => setOrigin(e.target.value)}
        >
          <MenuItem value={""}>None</MenuItem>
          {as_info && Sources.map((o, i) => {
            return (<MenuItem key={i} value={o}>{as_info[o]?.shortname}</MenuItem>)
          }
          )}
        </Select>
      </FormControl>
      <FormControl sx={{width: "15rem"}}>
        <InputLabel id="demo-simple-select-label">Sink</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={sink}
          label="Sink"
          onChange={e => setSink(e.target.value)}
        >
          <MenuItem value={""}>None</MenuItem>
          {Sinks.map((o, i) => (
            <MenuItem key={i} value={o}>{as_info[o]?.shortname}</MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
    <Box sx={{paddingLeft:"2rem"}}>
      {data && (
          <ForceGraph3D
            width={1450}
            height={550}
            graphData={data}
            linkSource='from'
            linkTarget='to'
            nodeLabel={d =>`${d.sname} (ASN: ${d.id})`}
            nodeAutoColorBy="country"
            // linkLabel={d => `${d.value * speedFactor} ms`}
            ref={graphRef}
            backgroundColor='#040D12'
            linkColor={d => {
              if (origin!="" && sink!=""){
                  if (d.origin == origin && d.sink == sink) {
                    return '#07f5e9'
                  }
                  else{
                    return '#222424'
                  }
              }
              else if (origin!="" || sink!=""){
                if (d.origin == origin || d.sink == sink) {
                  return '#07f5e9'
                }
                else{
                  return '#222424'
                }
              }
              else return '#222424'
            }}
            onNodeDragEnd={node => {
              node.fx = node.x
              node.fy = node.y
              node.fz = node.z
            }}
            linkWidth={d => {
              if (origin!="" && sink!=""){
                  if (d.origin == origin && d.sink == sink) {
                    return 3
                  }
                  else{
                    return 1
                  }
              }
              if (origin!="" || sink!=""){
                if (d.origin == origin || d.sink == sink) {
                  return 3
                }
                else{
                  return 1
                }
              }
              else return 1
            }}
            linkDirectionalParticles="value"
            linkDirectionalParticleSpeed={d => d.value * speedFactor}
            linkDirectionalParticleColor={d => {
              if (origin!="" && sink!=""){
                  if (d.origin == origin && d.sink == sink) {
                    return colors[d.color]
                  }
                  return '#222424'
              }
              if (origin!="" || sink!=""){
                if (d.origin == origin || d.sink == sink) {
                  return colors[d.color]
                }
                return '#222424'
              }
              else return colors[d.color]
            }}
            linkDirectionalParticleWidth={2}
            // linkCurvature={Math.random()*0.6-0.3}
          />
        )}
      </Box>
    </Box>
  )
}
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
/>  */}
export default App
