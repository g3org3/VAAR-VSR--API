;;for vdu in vdus
(and
  (< vdu.mem_size 600 MB )
  (< vdu.num_cpus 6 )
)
;;endfor

;;for cp in cps
(and
  (< cp.IP_address 10.100.0.110 )
  (> cp.IP_address 10.100.0.100 )
)
;;endfor