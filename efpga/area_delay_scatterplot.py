# import plotly.plotly as py
# import plotly.graph_objs as go
from statistics import mean
import matplotlib
# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
import numpy as np

ns0p5 = [0.5-float(x) for x in "-0.294 -0.314 -0.314 -0.313 -0.299 -0.296 -0.303 -0.307 -0.324 -0.312 -0.312 -0.319 -0.311 -0.321 -0.317 -0.308 -0.32 -0.299 -0.315 -0.313 -0.314 -0.312 -0.314 -0.324 -0.319 -0.301 -0.321 -0.318 -0.314 -0.311 -0.292 -0.301 -0.31 -0.299 -0.318 -0.309 -0.322 -0.312 -0.319 -0.316 -0.294 -0.311 -0.308 -0.317 -0.311 -0.305 -0.307 -0.318 -0.329 -0.315 -0.309 -0.302 -0.305 -0.318 -0.307 -0.314 -0.316 -0.32 -0.329 -0.324 -0.313 -0.311 -0.324 -0.315 -0.323 -0.318 -0.322 -0.316 -0.325 -0.323 -0.32 -0.323 -0.318 -0.304 -0.323 -0.318 -0.328 -0.322 -0.318 -0.319 -0.311 -0.308 -0.313 -0.316 -0.321 -0.325 -0.326 -0.322 -0.311 -0.313 -0.313 -0.329 -0.316 -0.332 -0.32 -0.319 -0.292 -0.311 -0.314 -0.315 -0.328 -0.318 -0.325 -0.331 -0.305 -0.292 -0.317 -0.32 -0.314 -0.298 -0.297 -0.309 -0.31 -0.318 -0.305 -0.325 -0.314 -0.313 -0.305 -0.325 -0.305 -0.319 -0.327 -0.322 -0.311 -0.325 -0.323 -0.304 -0.309 -0.305 -0.322 -0.322 -0.324 -0.324 -0.324 -0.325 -0.328 -0.316 -0.314 -0.326 -0.327 -0.327 -0.327 -0.319 -0.318 -0.32 -0.315 -0.327 -0.32 -0.321 -0.322 -0.317 -0.318 -0.323 -0.326 -0.31 -0.319 -0.323 -0.315 -0.324 -0.318 -0.319 -0.338 -0.303 -0.31 -0.301 -0.324 -0.303 -0.312 -0.31 -0.299 -0.324 -0.304 -0.315 -0.319 -0.32 -0.299 -0.299 -0.301 -0.316 -0.321 -0.329 -0.325 -0.296 -0.317 -0.319 -0.29 -0.304 -0.314 -0.311 -0.318 -0.327 -0.293 -0.294 -0.306 -0.325 -0.321 -0.291 -0.305 -0.324 -0.315 -0.317 -0.303 -0.326 -0.322 -0.31 -0.297 -0.324 -0.311 -0.307 -0.311 -0.318 -0.314 -0.293 -0.323 -0.337 -0.312 -0.294 -0.326 -0.314 -0.315 -0.328 -0.318 -0.331 -0.328 -0.332 -0.322 -0.314 -0.332 -0.327 -0.329 -0.328 -0.328 -0.327 -0.327 -0.324 -0.322 -0.327 -0.325 -0.321 -0.329 -0.327 -0.327 -0.33 -0.337 -0.32 -0.32 -0.322 -0.33 -0.319 -0.33 -0.325 -0.327 -0.314 -0.326 -0.317 -0.313 -0.312 -0.321 -0.315 -0.322 -0.328 -0.316 -0.321 -0.315 -0.322 -0.328 -0.316 -0.315 -0.308 -0.303 -0.31 -0.306 -0.307 -0.31 -0.305 -0.308 -0.314 -0.303 -0.304 -0.312 -0.324 -0.312 -0.309 -0.312 -0.304 -0.314 -0.329 -0.32 -0.319 -0.314 -0.321 -0.336 -0.321 -0.317 -0.322 -0.327 -0.318 -0.324 -0.315 -0.32 -0.293 -0.316 -0.309 -0.316 -0.331 -0.322 -0.324 -0.307 -0.31 -0.327 -0.323 -0.315 -0.308 -0.312 -0.314 -0.327 -0.324 -0.315 -0.305 -0.305 -0.307 -0.313 -0.321 -0.305 -0.321 -0.315 -0.318 -0.314 -0.327 -0.303 -0.309 -0.324 -0.316 -0.325 -0.315 -0.295 -0.306 -0.309 -0.305 -0.303 -0.308 -0.303 -0.305 -0.293 -0.316 -0.315 -0.313 -0.282 -0.307 -0.321 -0.296 -0.286 -0.324 -0.33 -0.32 -0.313 -0.32 -0.308 -0.327 -0.317 -0.307 -0.296 -0.318 -0.291 -0.309 -0.305 -0.308 -0.295 -0.314 -0.291 -0.296 -0.32 -0.324 -0.303 -0.299 -0.3 -0.293 -0.314 -0.311 -0.314 -0.312 -0.323 -0.311 -0.323 -0.32 -0.313 -0.319 -0.309 -0.317 -0.319 -0.317 -0.326 -0.314 -0.309 -0.319 -0.321 -0.326 -0.32 -0.298 -0.322 -0.305 -0.301 -0.319 -0.315 -0.312 -0.304 -0.304 -0.321 -0.322 -0.308 -0.321 -0.321 -0.319 -0.317 -0.32 -0.322 -0.325 -0.322 -0.3 -0.317 -0.311 -0.305 -0.318 -0.32 -0.312 -0.322 -0.323 -0.313 -0.304 -0.311 -0.318 -0.322 -0.304 -0.297 -0.312 -0.3 -0.322 -0.31 -0.326 -0.304 -0.315 -0.32 -0.319 -0.326 -0.326 -0.322 -0.316 -0.315 -0.328 -0.317 -0.307 -0.316 -0.325 -0.323 -0.314 -0.306 -0.325 -0.323 -0.312 -0.321 -0.319 -0.316 -0.332 -0.331 -0.327 -0.311 -0.313 -0.327 -0.306 -0.315 -0.325 -0.327 -0.316 -0.31 -0.317 -0.323 -0.33 -0.319 -0.309 -0.323 -0.322 -0.314 -0.314 -0.322 -0.323 -0.328 -0.313 -0.301 -0.316 -0.324 -0.312 -0.328 -0.308 -0.321 -0.322 -0.314 -0.319 -0.327 -0.311 -0.332 -0.316 -0.325 -0.318 -0.323 -0.329 -0.32 -0.319 -0.331 -0.322 -0.33 -0.314 -0.306 -0.326 -0.328 -0.32 -0.316 -0.323 -0.284 -0.318 -0.308 -0.314 -0.316 -0.32 -0.314 -0.317 -0.319 -0.331 -0.32 -0.31 -0.31 -0.312 -0.312 -0.311 -0.283 -0.291 -0.309 -0.309 -0.317 -0.32 -0.333 -0.328 -0.315 -0.32 -0.312 -0.327 -0.33 -0.311 -0.323 -0.317 -0.321 -0.317 -0.322 -0.322 -0.316 -0.327 -0.325 -0.319 -0.323 -0.323 -0.32 -0.322 -0.306 -0.32 -0.318 -0.319 -0.32 -0.31 -0.31 -0.324 -0.32 -0.316 -0.316 -0.322 -0.315 -0.302 -0.335 -0.324 -0.337 -0.314 -0.329 -0.329 -0.329 -0.335 -0.316 -0.286 -0.307 -0.311 -0.311 -0.303 -0.304 -0.297 -0.308 -0.294 -0.294 -0.305 -0.319 -0.311 -0.299 -0.3 -0.304 -0.307 -0.3 -0.309 -0.311 -0.306 -0.307 -0.307 -0.307 -0.311 -0.306 -0.314 -0.323 -0.324 -0.312 -0.313 -0.303 -0.31 -0.302 -0.321 -0.296 -0.319 -0.316 -0.314 -0.314 -0.319 -0.321 -0.324 -0.31 -0.316 -0.303 -0.307 -0.302 -0.311 -0.323 -0.314 -0.306 -0.298 -0.298 -0.312 -0.319 -0.299 -0.302 -0.293 -0.322 -0.288 -0.303 -0.305 -0.298 -0.31 -0.323".split()]
ns0p6 = [0.6-float(x) for x in "-0.207 -0.198 -0.202 -0.207 -0.219 -0.218 -0.213 -0.216 -0.214 -0.244 -0.213 -0.2 -0.223 -0.241 -0.217 -0.215 -0.246 -0.237 -0.235 -0.237 -0.246 -0.258 -0.242 -0.252 -0.243 -0.243 -0.261 -0.239 -0.251 -0.245 -0.241 -0.236 -0.237 -0.249 -0.259 -0.238 -0.242 -0.238 -0.241 -0.238 -0.249 -0.241 -0.218 -0.235 -0.245 -0.221 -0.243 -0.24 -0.238 -0.226 -0.234 -0.242 -0.227 -0.241 -0.242 -0.247 -0.234 -0.245 -0.238 -0.249 -0.234 -0.241 -0.237 -0.242 -0.231 -0.226 -0.191 -0.232 -0.197 -0.215 -0.222 -0.213 -0.242 -0.249 -0.245 -0.25 -0.246 -0.234 -0.233 -0.243 -0.254 -0.241 -0.236 -0.248 -0.234 -0.232 -0.235 -0.239 -0.243 -0.243 -0.23 -0.24 -0.246 -0.241 -0.244 -0.234 -0.245 -0.242 -0.246 -0.236 -0.243 -0.246 -0.229 -0.226 -0.234 -0.226 -0.228 -0.247 -0.231 -0.234 -0.22 -0.227 -0.244 -0.242 -0.246 -0.247 -0.241 -0.24 -0.244 -0.234 -0.218 -0.239 -0.221 -0.231 -0.228 -0.234 -0.229 -0.234 -0.251 -0.251 -0.247 -0.249 -0.244 -0.253 -0.24 -0.252 -0.255 -0.253 -0.246 -0.24 -0.248 -0.252 -0.234 -0.227 -0.225 -0.234 -0.24 -0.238 -0.244 -0.239 -0.235 -0.228 -0.24 -0.235 -0.234 -0.238 -0.243 -0.239".split()]
ns0p75 = [0.75-float(x) for x in "-0.122 -0.126 -0.138 -0.132 -0.137 -0.12 -0.131 -0.13 -0.101 -0.125 -0.126 -0.113 -0.124 -0.136 -0.128 -0.121 -0.152 -0.152 -0.154 -0.146 -0.153 -0.144 -0.147 -0.142 -0.152 -0.158 -0.127 -0.128 -0.129 -0.139 -0.13 -0.135 -0.113 -0.126 -0.149 -0.133 -0.151 -0.153 -0.143 -0.164 -0.153 -0.143 -0.149 -0.163 -0.169 -0.162 -0.12 -0.139 -0.143 -0.128 -0.146 -0.152 -0.153 -0.138 -0.137 -0.157 -0.139 -0.137 -0.159 -0.143 -0.124 -0.119 -0.121 -0.146 -0.151 -0.158 -0.163 -0.142 -0.133 -0.128 -0.162 -0.157 -0.146 -0.168 -0.15 -0.152 -0.156 -0.153 -0.148 -0.153 -0.155 -0.156 -0.132 -0.135 -0.153 -0.157 -0.144 -0.155 -0.147 -0.156 -0.153 -0.131 -0.139 -0.141 -0.15 -0.159 -0.161 -0.151 -0.158 -0.128 -0.142 -0.151 -0.145 -0.148 -0.136 -0.162 -0.152 -0.159 -0.16 -0.129 -0.149 -0.148 -0.152 -0.145 -0.133 -0.154 -0.132 -0.145 -0.147 -0.148 -0.154 -0.15 -0.15 -0.155 -0.142 -0.152 -0.144 -0.149 -0.146 -0.14 -0.154 -0.148 -0.139 -0.153 -0.141 -0.171 -0.156 -0.133 -0.16 -0.16 -0.16 -0.159 -0.155 -0.154 -0.142 -0.149 -0.153 -0.154 -0.166 -0.156 -0.156 -0.147 -0.16 -0.146 -0.137 -0.161 -0.138 -0.152 -0.156 -0.153 -0.161 -0.166 -0.161 -0.155 -0.162 -0.161".split()]
ns0p9 = [0.9-float(x) for x in "-0.033 -0.013 -0.011 -0.027 -0.006 -0.019 -0.021 -0.033 0.038 0.033 -0.007 -0.003 -0.0 -0.0 0.008 0.002 -0.022 -0.021 -0.024 -0.021 -0.018 -0.024 -0.009 -0.024 -0.023 -0.021 -0.014 -0.027 -0.023 -0.02 -0.022 0.006 -0.013 -0.03 -0.032 -0.025 -0.014 -0.028 -0.02 -0.003 0.008 -0.003 0.005 -0.026 -0.018 -0.015 -0.019 -0.024 -0.027 -0.024 -0.012 -0.014 -0.023 -0.024 -0.015 -0.027 -0.014 -0.026 -0.01 -0.008 0.003 -0.003 -0.012 -0.022 -0.025 0.036 0.036 -0.004 0.028 0.02 0.027 0.02 -0.023 -0.03 -0.023 -0.041 -0.033 -0.012 -0.036 -0.038 -0.047 -0.034 -0.017 -0.016 -0.016 -0.022 -0.032 -0.03 -0.022 -0.024 -0.022 -0.024 -0.013 -0.002 -0.024 -0.027 0.014 -0.015 -0.001 -0.006 -0.02 -0.02 -0.012 -0.017 -0.031 -0.02 -0.024 -0.008 -0.022 -0.032 -0.009 -0.022 -0.034 -0.031 -0.005 -0.03 -0.034 -0.022 -0.01 -0.024 -0.0 0.003 -0.011 -0.03 -0.027 -0.029 -0.009 0.0 -0.04 -0.026 -0.057 -0.029 -0.023 -0.035 -0.028 -0.036 -0.039 -0.031 -0.027 -0.032 -0.038 -0.011 -0.027 -0.034 -0.028 -0.04 -0.025 -0.018 -0.008 -0.012 0.006 -0.019 -0.02 -0.016 -0.03 -0.028 -0.023 -0.023 -0.014 -0.033 -0.034 -0.021 -0.033 -0.021 -0.03".split()]
ns1p0 = [1-float(x) for x in "-0.004 -0.024 -0.004 0.016 0.038 0.008 -0.024 -0.016 0.009 0.005 -0.005 0.013 0.006 0.001 0.019 0.014 -0.003 0.013 0.002 0.006 0.005 0.005 0.004 0.012 -0.002 0.008 0.016 0.009 0.034 -0.005 0.021 0.016 0.002 0.01 0.01 0.006 -0.004 0.008 -0.007 0.0 0.003 -0.004 0.019 0.002 -0.005 -0.005 0.001 -0.0 0.002 -0.003 0.014 0.004 -0.007 -0.004 0.011 0.001 0.013 0.002 0.001 0.001 0.017 -0.006 0.022 0.0 0.071 0.003 0.044 0.04 0.015 0.016 0.002 0.039 0.003 -0.004 0.002 -0.004 0.011 0.003 -0.006 0.0 0.013 0.001 0.003 0.0 0.005 -0.004 0.003 0.0 0.013 0.004 0.0 0.013 0.023 0.009 0.008 -0.005 -0.008 0.021 0.007 0.007 0.0 0.004 0.025 -0.005 -0.004 0.011 0.001 0.027 -0.007 -0.001 -0.001 -0.0 -0.004 0.017 0.012 0.01 0.002 0.024 0.022 0.01 0.038 0.01 0.004 0.051 -0.002 0.018 0.029 0.035 0.002 0.002 0.004 -0.001 0.025 -0.01 -0.004 0.003 -0.001 0.007 0.002 0.003 -0.007 -0.005 -0.006 -0.0 -0.002 -0.002 0.007 0.007 0.001 0.014 -0.002 0.011 -0.003 0.002 0.007 -0.001 0.004 -0.006 0.014 -0.007 -0.007 -0.0 -0.005 0.0 -0.008 -0.004 0.004".split()]
ns1p25 = [1.25-float(x) for x in "0.116 0.182 0.082 0.107 0.117 0.101 0.121 0.121 0.148 0.033 0.062 0.101 0.057 0.09 0.078 0.048 0.01 0.01 0.001 0.011 -0.002 0.02 0.019 0.01 0.005 -0.001 0.044 0.052 0.017 0.058 0.043 0.045 0.029 0.014 0.004 0.028 0.01 0.006 0.02 0.028 0.018 0.001 0.012 0.008 0.002 0.023 0.03 0.054 0.042 0.034 0.053 0.027 0.007 -0.003 0.038 0.068 0.181 0.07 0.046 0.007 0.039 0.07 0.129 0.156 0.178 0.045 0.05 0.18 0.076 0.187 0.109 0.161 0.019 0.004 0.005 0.011 0.022 0.012 0.007 0.015 0.0 0.004 0.006 0.007 0.005 -0.005 0.008 0.0 0.009 0.005 -0.002 -0.001 0.004 0.014 0.032 0.019 0.014 0.007 0.011 0.023 0.028 0.002 0.001 0.01 0.032 0.021 0.025 -0.0 0.002 0.011 0.009 -0.003 0.047 0.02 0.028 0.087 0.043 0.032 0.054 0.033 0.146 0.083 0.041 0.081 0.092 0.052 0.174 0.074 0.029 0.008 0.021 0.008 0.009 0.013 0.0 0.016 0.018 0.009 0.027 -0.005 0.018 0.006 0.009 0.017 0.004 0.002 0.004 0.005 0.058 0.026 0.03 0.05 0.055 0.032 0.044 0.006 0.035 0.031 0.018 0.047 0.0 0.02 0.014 0.032 0.009 0.015 0.0 0.01".split()]
ns1p5 = [1.5-float(x) for x in "0.233 0.292 0.242 0.217 0.301 0.216 0.226 0.195 0.217 0.103 0.158 0.201 0.168 0.185 0.153 0.094 0.013 0.02 0.014 0.013 0.011 0.006 0.027 0.028 0.025 0.028 0.127 0.125 0.044 0.053 0.013 0.021 0.048 0.053 0.058 0.088 0.022 0.003 0.021 0.092 0.01 0.023 0.028 0.038 0.002 0.055 0.074 0.081 0.022 0.036 0.057 0.016 -0.009 0.004 0.042 0.089 0.242 0.101 0.14 0.133 0.141 0.175 0.25 0.173 0.327 0.258 0.218 0.237 0.22 0.292 0.284 0.322 0.019 -0.003 0.008 0.023 0.009 0.027 0.015 0.017 0.01 0.022 0.092 0.087 0.024 0.058 0.051 0.028 0.038 0.042 0.017 0.02 0.05 0.02 0.027 0.062 0.023 0.023 0.018 0.064 0.029 0.015 0.058 0.027 0.096 0.043 0.039 0.05 0.007 0.017 0.018 -0.001 0.213 0.152 0.11 0.236 0.139 0.148 0.199 0.185 0.289 0.172 0.187 0.197 0.152 0.166 0.28 0.209 0.068 0.017 0.011 0.046 0.093 0.048 0.011 0.009 0.041 0.023 0.036 0.004 0.045 0.05 0.012 0.036 0.017 0.057 0.032 -0.001 0.105 0.009 0.069 0.106 0.097 0.089 0.107 0.045 0.014 0.026 0.062 0.07 0.035 0.135 0.043 0.13 0.02 0.121 0.044 0.037".split()]
ns2p0 = [2-float(x) for x in "0.544 0.626 0.542 0.609 0.577 0.515 0.529 0.52 0.561 0.612 0.589 0.512 0.547 0.574 0.564 0.481 0.328 0.269 0.277 0.319 0.277 0.247 0.306 0.333 0.352 0.268 0.403 0.46 0.416 0.36 0.365 0.411 0.412 0.35 0.301 0.224 0.327 0.373 0.404 0.462 0.428 0.398 0.416 0.45 0.393 0.48 0.417 0.362 0.37 0.412 0.388 0.37 0.346 0.341 0.349 0.38 0.511 0.572 0.502 0.478 0.469 0.384 0.564 0.604 0.594 0.637 0.597 0.581 0.607 0.611 0.55 0.557 0.329 0.365 0.344 0.348 0.346 0.4 0.411 0.354 0.398 0.259 0.41 0.415 0.28 0.216 0.225 0.249 0.246 0.26 0.202 0.212 0.38 0.349 0.394 0.403 0.386 0.397 0.421 0.462 0.453 0.343 0.399 0.367 0.494 0.342 0.333 0.325 0.366 0.351 0.365 0.32 0.504 0.501 0.474 0.462 0.555 0.449 0.45 0.52 0.626 0.598 0.551 0.564 0.584 0.535 0.637 0.579 0.325 0.311 0.307 0.327 0.423 0.364 0.267 0.323 0.256 0.258 0.447 0.353 0.47 0.548 0.445 0.484 0.409 0.457 0.302 0.394 0.465 0.335 0.411 0.48 0.505 0.492 0.508 0.426 0.439 0.432 0.472 0.42 0.31 0.424 0.313 0.458 0.39 0.399 0.323 0.353".split()]

timings = [ns0p5, ns0p6, ns0p75, ns0p9, ns1p0, ns1p25, ns1p5, ns2p0]
# timings = [ns0p5, ns0p6, ns0p75, ns0p9, ns1p0, ns1p25, ns1p5]
timings = [ns0p5, ns0p6, ns0p75, ns0p9, ns1p0, ns1p25, ns2p0]

matplotlib.rcParams.update({'font.size': 13})

# get x and y vectors
areas = [423712.296, 403621.092, 372627.234, 347884.488, 319424.868, 289984.842, 283717.350, 285440.022]
# areas = [423712.296, 403621.092, 372627.234, 347884.488, 319424.868, 289984.842, 283717.350]
areas = [423712.296, 403621.092, 372627.234, 347884.488, 319424.868, 289984.842, 285440.022]

areas = [area/1000000 for area in areas]

delay_obt = [mean(timing) for timing in timings]
delay_target = [0.5, 0.6, 0.75, 0.9, 1, 1.25, 1.5, 2]
# delay_target = [0.5, 0.6, 0.75, 0.9, 1, 1.25, 1.5]
delay_target = [0.5, 0.6, 0.75, 0.9, 1, 1.25, 2]

# calculate polynomial
z_obt = np.polyfit(areas, delay_obt, 2)
f_obt = np.poly1d(z_obt)
z_target = np.polyfit(areas, delay_target, 3)
f_target = np.poly1d(z_target)

# calculate new x's and y's
x_new = np.linspace(min(areas), max(areas), 50)
y_obt = f_obt(x_new)
y_target = f_target(x_new)

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(areas, delay_target,'x', markersize=10, color = 'red', label='Targeted delay')
ax.plot(areas, delay_obt,'o', color = 'royalblue', linestyle='-', label='Obtained delay')


# ax.set_xlim([0.28, 0.5])

plt.legend(loc='upper right', fontsize=13)
plt.xlabel("Area (mm$^2$)", fontsize=13)
plt.ylabel("Path delay (ns)", fontsize=13)

for i in range(len(delay_target)):
    if i not in [3, 4, 5]:
        plt.annotate(
            '', xy=(areas[i], delay_target[i]), xycoords='data',
            xytext=(areas[i], delay_obt[i]), textcoords='data',
            arrowprops={'arrowstyle': '<-'})

ax.set_xlim([0.27, 0.44])
plt.grid(True)
plt.show()

# pylab.title('Polynomial Fit with Matplotlib')
# ax = plt.gca()
# ax.set_axis_bgcolor((0.898, 0.898, 0.898))
# fig = plt.gcf()
# py.plot_mpl(fig, filename='polynomial-Fit-with-matplotlib')