{
	"targets": [
    	{
        	"target_name": "nodex21s",
        	"sources": [
      	    	"multihashing.cc",
				"sha3/aes_helper.c",
				"sha3/blake.c",
				"sha3/bmw.c",
				"sha3/cubehash.c",
				"sha3/echo.c",
				"sha3/extra.c",
				"sha3/fugue.c",
				"sha3/gost_streebog.c",
				"sha3/groestl.c",
				"sha3/hamsi.c",
				"sha3/haval.c",
				"sha3/jh.c",
				"sha3/keccak.c",
				"sha3/luffa.c",
				"sha3/lyra2.c",
				"sha3/sha2.c",
				"sha3/shabal.c",
				"sha3/shavite.c",
				"sha3/simd.c",
				"sha3/skein.c",
				"sha3/sph_sha2big.c",
				"sha3/sph_sha2.c",
				"sha3/sponge.c",
				"sha3/tiger.c",
				"sha3/whirlpool.c",
	        	"x21s.c",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++11"
            ],
        }
    ]
}
