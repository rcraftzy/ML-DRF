import { connect } from "react-redux"
import {SpeakerphoneIcon} from "@heroicons/react/solid"

function Alert({alert}) {
  const displayAlert = () => {
    if (alert !== null) {
      return ( 
        <div>
          <div className="fixed z-50 buttom-0 inset-x-0 pb-2 sm:pb-5">
          <div className="max-w-7x mx-auto px-3 sm:px-6 lg:px-8">
              <div className={`p-2 rounded-lg bg-${alert.alertType}-600 shadown-lg sm:p-3`}>
                <span className={`flex p-2 rounded-lg bg-${alert.alertType}-600`}>
                  <SpeakerphoneIcon
                    className="h-6 w-6 text-white"
                    aria-hidden="true"
                  />
                </span>
                <p className="ml-3 font-medium text-white">
                  <span className="md:hidden text-white">
                    {alert.msg}
                  </span>
                  <sapn>
                    {alert.msg}
                  </sapn>
                </p>
              </div>
            </div>
          </div>
        </div>
      )
    }else{
      return <></>
    }
  }
  return <>{displayAlert()}</>
}

const mapStateToProps = (state) => ({
  alert: state.alert.alert
})

export default connect(mapStateToProps)(Alert)
