import math

def chunk_latency(chunk_s, rtf, rtt_s):
    return chunk_s + (rtf * chunk_s) + rtt_s

def largest_chunk_under(budget_s, rtf, rtt_s, step=0.05):
    n = 1
    while chunk_latency(step * n, rtf, rtt_s) <= budget_s + 1e-12:
        n+=1

    if n==1:
        return None
    
    return round((n-1) * step ,2)

def concurrent_streams(rtf, gpu_share=1.0):
    return math.floor(gpu_share/rtf)

def end_of_speech_latency(hangover_s, chunk_s, rtf, rtt_s):
    return hangover_s + chunk_latency(chunk_s, rtf, rtt_s)

def budget_breakdown(chunk_s, rtf, rtt_s):
    # TODO: {'wait', 'model', 'network'} fractions rounded to 4 decimals
    return {'wait': round(chunk_s/chunk_latency(chunk_s, rtf, rtt_s),4),
            'model': round((chunk_s*rtf)/chunk_latency(chunk_s, rtf, rtt_s),4),
            'network': round(rtt_s/chunk_latency(chunk_s, rtf, rtt_s),4)}
