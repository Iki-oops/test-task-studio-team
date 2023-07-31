import { useTheme } from "@emotion/react";
import { ResponsiveBar } from '@nivo/bar'
import { tokens } from '../theme'; 
import { useHttp } from "../hooks";
import { useEffect, useState } from "react";

const BarChart = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const { request } = useHttp();
  const [data, setData] = useState([]);
  const [commands, setCommands] = useState([])

  useEffect(() => {
    request('http://localhost:8000/api/messages/detail-statistics/')
      .then(result => {setData(result.map(item => ({date: item.date, ...item.commands})))})
      .catch(console.log)
    request('http://localhost:8000/api/messages/commands/')
      .then(setCommands)
      .catch(console.log)
  }, [])

  return (
    <ResponsiveBar
        data={data}
        theme={{
          axis: {
            domain: {
              line: {
                stroke: colors.grey[100]
              }
            },
            legend: {
              text: {
                fill: colors.grey[100]
              }
            },
            ticks: {
              line: {
                stroke: colors.grey[100],
                strokeWidth: 1,
              },
              text: {
                fill: colors.grey[100]
              }
            }
          },
          legends: {
            text: {
              fill: colors.grey[100]
            }
          }
        }}
        keys={commands}
        indexBy="date"
        margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
        padding={0.15}
        valueScale={{ type: 'linear' }}
        indexScale={{ type: 'band', round: true }}
        colors={{ scheme: 'nivo' }}
        borderColor={{
            from: 'color',
            modifiers: [
                [
                    'darker',
                    1.6
                ]
            ]
        }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'Даты',
            legendPosition: 'middle',
            legendOffset: 32
        }}
        axisLeft={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'Команды',
            legendPosition: 'middle',
            legendOffset: -40
        }}
        labelSkipWidth={12}
        labelSkipHeight={12}
        labelTextColor={{
            from: 'color',
            modifiers: [
                [
                    'darker',
                    1.6
                ]
            ]
        }}
        legends={[
            {
                dataFrom: 'keys',
                anchor: 'bottom-right',
                direction: 'column',
                justify: false,
                translateX: 120,
                translateY: 0,
                itemsSpacing: 2,
                itemWidth: 100,
                itemHeight: 20,
                itemDirection: 'left-to-right',
                itemOpacity: 0.85,
                symbolSize: 20,
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemOpacity: 1
                        }
                    }
                ]
            }
        ]}
        role="application"
        ariaLabel="Nivo bar chart demo"
        barAriaLabel={e=>e.id+": "+e.formattedValue+" in country: "+e.indexValue}
    />
  )
}

export default BarChart;
