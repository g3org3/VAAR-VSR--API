;;for vdu in vdus
(and
  (< vdu.mem_size 1 GB )
  (< vdu.num_cpus 6 )
)
;;endfor

;;for cp in cps
(and
  (< cp.IP_address 10.100.0.106 )
  (> cp.IP_address 10.100.0.100 )
)
;;endfor