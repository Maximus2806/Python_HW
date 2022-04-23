def dec_to_bin(num):
    num_bin = []
    while num != 0:
        rest = num % 2
        if rest == 0:
            num_bin.append(0)
        else:
            num_bin.append(1)
        num = num // 2
    num_bin.reverse()
    res_bin = ''.join(str(e) for e in num_bin)
    return res_bin


def bin_to_dec(str_bin):
    m_power = len(str_bin) - 1
    res_dec = 0
    for i in str_bin:
        if int(i) == 0 and m_power == 0:
            continue
        else:
            res_dec += (int(i) * 2) ** m_power
            m_power -= 1
    return res_dec





